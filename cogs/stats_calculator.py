from typing import Literal

import discord
from discord import app_commands
from discord.ext import commands

from utils.autocomplete.pokemon_autocomplete import pokemon_autocomplete
from utils.functions.pokeapi_func import get_pokemon_stats
from utils.functions.pokemon_func import get_display_name
from utils.logs.debug_log import debug_enabled, debug_log, enable_debug
from utils.logs.pretty_log import pretty_log
from utils.visuals.get_pokemon_gifs import get_pokemon_gif
from utils.visuals.pretty_defer import pretty_defer
from utils.visuals.type_embed import get_type_embed_color

#enable_debug(f"{__name__}.stats_calculator")


def calculate_non_hp(base_stat, iv, ev, lvl):
    """
    Calculate non-HP stat using the provided formula:
    stat = lvl/100 * (base_stat * 2.7 + iv + floor(ev/4)) + iv + 5
    Rounds down ev/4 and the final result.
    """
    from math import floor

    stat = (lvl / 100) * (base_stat * 2.7 + iv + floor(ev / 4)) + iv + 5
    return floor(stat)


def calculate_hp(base_hp, iv, ev, lvl):
    """
    Calculate HP stat using the provided formula:
    HP = lvl * [ (base_hp * 2.7 + iv + floor(ev/4)) / 100 + 1 ] + 10
    Rounds down ev/4 and the final result.
    """
    from math import floor

    hp = lvl * ((base_hp * 2.7 + iv + floor(ev / 4)) / 100 + 1) + 10
    return floor(hp)


class StatsCalculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        debug_log("StatsCalculator cog initialized.")

    @app_commands.command(
        name="stats-calculator",
        description="Calculate Pokémon stats based on IVs, EVs, and level.",
    )
    @app_commands.autocomplete(pokemon=pokemon_autocomplete)
    @app_commands.describe(
        pokemon="The name of the Pokémon.",
        stat="The stat to calculate (hp, attack, defense, special-attack, special-defense, speed).",
        ivs="The Individual Values (IVs) for the stat.",
        evs="The Effort Values (EVs) for the stat.",
        level="The level of the Pokémon.",
    )
    async def stats_calculator(
        self,
        interaction: discord.Interaction,
        pokemon: str,
        stat: Literal[
            "hp",
            "attack",
            "defense",
            "special-attack",
            "special-defense",
            "speed",
        ],
        ivs: int,
        evs: int,
        level: int,
    ):
        # Defer the response to give us more time to calculate
        loader = await pretty_defer(
            interaction=interaction, content="Calculating stats...", ephemeral=False
        )
        debug_log(
            f"Received stats-calculator command: pokemon={pokemon}, stat={stat}, ivs={ivs}, evs={evs}, level={level}"
        )
        debug_log(
            f"Calculating stats for {pokemon} - Stat: {stat}, IVs: {ivs}, EVs: {evs}, Level: {level}"
        )
        # Check if golden prefix is present
        is_golden = pokemon.lower().startswith("golden ")
        debug_log(f"Is golden: {is_golden}")
        if not is_golden and ivs > 15:
            debug_log(f"Invalid IVs for non-golden Pokémon: {ivs}")
            await loader.edit(
                content="IVs cannot be greater than 15 for non-golden Pokémon."
            )
            return

        # Check if EVs are within valid range
        if evs < 0 or evs > 255:
            debug_log(f"Invalid EVs: {evs}")
            await loader.error(content="EVs must be between 0 and 255.")
            return

        # Fetch base stats from cache or API
        try:
            base_stats = await get_pokemon_stats(self.bot, pokemon, is_golden)
            debug_log(f"Fetched base stats: {base_stats}")
            required_keys = [
                "base_hp",
                "base_atk",
                "base_spe",
                "base_spa",
                "base_def",
                "base_spd",
            ]
            if not base_stats or any(base_stats.get(k) is None for k in required_keys):
                await loader.error(
                    content="Could not fetch valid base stats for the specified Pokémon."
                )
                debug_log(f"Base stats missing or invalid for {pokemon}: {base_stats}")
                return
            debug_log(f"Base stats found for {pokemon}, continuing calculation.")
        except Exception as e:
            pretty_log("error", f"Error fetching stats for {pokemon}: {str(e)}")
            debug_log(f"Exception occurred while fetching stats: {str(e)}")
            await loader.error(content=f"Error fetching stats: {str(e)}")
            return

        embed_color = get_type_embed_color(pokemon)
        debug_log(f"Embed color resolved: {embed_color}")
        if not embed_color:
            pretty_log(
                "warn",
                f"Could not determine embed color for {pokemon}. Defaulting to blue.",
            )
            embed_color = discord.Color.blue()

        debug_log("Starting stat calculation block.")

        # Calculate the requested stat
        try:
            if stat == "hp":
                calculated_stat = calculate_hp(base_stats["base_hp"], ivs, evs, level)
                debug_log(f"Calculated HP: {calculated_stat}")
            else:
                stat_key_map = {
                    "attack": "base_atk",
                    "defense": "base_def",
                    "special-attack": "base_spa",
                    "special-defense": "base_spd",
                    "speed": "base_spe",
                }
                stat_key = stat_key_map.get(stat)
                if stat_key is None:
                    raise KeyError(f"Unknown stat key for stat '{stat}'")
                calculated_stat = calculate_non_hp(
                    base_stats[stat_key], ivs, evs, level
                )
                debug_log(f"Calculated {stat}: {calculated_stat}")
            debug_log(
                f"Stat calculation complete for {pokemon}: {stat} = {calculated_stat}"
            )
        except Exception as e:
            pretty_log("error", f"Error calculating stat for {pokemon}: {str(e)}")
            debug_log(f"Exception occurred during stat calculation: {str(e)}")
            await loader.error(content=f"Error calculating stat: {str(e)}")
            return

        debug_log("Building embed and preparing response.")
        display_name = get_display_name(pokemon)
        debug_log(f"Display name resolved: {display_name}")
        desc = (
            f"> - **Stat:** {stat.replace('-', ' ').title()}\n"
            f"> - **IVs:** {ivs}\n"
            f"> - **EVs:** {evs}\n"
            f"> - **Level:** {level}\n"
            f"> - **Total:** {stat.replace('-', ' ').title()}: **{calculated_stat}**"
        )
        # Embed the result
        embed = discord.Embed(
            title=f"Stats Calculator",
            color=embed_color,
        )
        embed.set_author(
            name=interaction.user.display_name,
            icon_url=interaction.user.display_avatar.url,
        )
        embed.add_field(name=display_name, value=desc, inline=False)
        image_url = get_pokemon_gif(pokemon)
        debug_log(f"Image URL resolved: {image_url}")
        if image_url:
            embed.set_thumbnail(url=image_url)

        debug_log("Calling loader.success to send embed response.")

        await loader.success(content="", embed=embed)

    debug_log("Embed response sent successfully.")


async def setup(bot):
    await bot.add_cog(StatsCalculator(bot))
