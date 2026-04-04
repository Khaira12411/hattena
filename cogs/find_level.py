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

"""enable_debug(f"{__name__}.find_level")
enable_debug(f"{__name__}.estimate_level_and_iv_from_hp")"""


def estimate_level_and_iv_from_hp(pokemon, hp, base_hp, is_golden=False, max_level=500):
    """
    Estimate possible level(s) and IV range for a Pokémon given its HP stat.
    Assumes EV = 0. Returns a dict: {level: [possible_ivs]} for all levels up to max_level where the HP matches.
    Args:
        pokemon (str): Name of the Pokémon (for reference, not used in calculation).
        hp (int): Observed HP stat.
        base_hp (int): Base HP stat of the Pokémon.
        is_golden (bool): If True, max IV is 20; else 15.
        max_level (int): Maximum level to check (default 200).
    Returns:
        dict: {level: [possible_ivs]} for all levels up to max_level where the HP matches.
    """
    from math import floor

    debug_log(
        f"Estimating level/IVs for {pokemon} | HP={hp} | base_hp={base_hp} | is_golden={is_golden} | max_level={max_level}"
    )

    max_iv = 20 if is_golden else 15
    debug_log(f"Max IV set to {max_iv}")
    possible = {}
    for lvl in range(1, max_level + 1):
        ivs = []
        for iv in range(0, max_iv + 1):
            # HP = lvl * [ (base_hp * 2.7 + iv) / 100 + 1 ] + 10
            calc_hp = floor(lvl * (((base_hp * 2.7 + iv) / 100) + 1) + 10)
            if calc_hp == hp:
                debug_log(f"Match found: Level {lvl}, IV {iv}")
                ivs.append(iv)
        if ivs:
            possible[lvl] = ivs
    debug_log(f"Possible level/IVs: {possible}")
    return possible


class FindLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        debug_log("FindLevel cog initialized.")

    @app_commands.command(
        name="find-level",
        description="Determines the level of a Pokemon based on its hp. (Assumes 0 Evs)",
    )
    @app_commands.autocomplete(pokemon=pokemon_autocomplete)
    @app_commands.describe(
        pokemon="The name of the Pokémon.",
        hp="The current HP of the Pokémon.",
    )
    async def find_level(
        self,
        interaction: discord.Interaction,
        pokemon: str,
        hp: int,
    ):
        # Defer the response to give us more time to calculate
        loader = await pretty_defer(
            interaction=interaction, content="Calculating stats...", ephemeral=False
        )

        # Check if golden prefix is present
        is_golden = pokemon.lower().startswith("golden ")
        debug_log(f"Is golden: {is_golden}")

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
        # Calculate possible levels and IVs based on the provided HP
        possible = estimate_level_and_iv_from_hp(
            pokemon, hp, base_stats["base_hp"], is_golden
        )
        top_line = f"- **HP:** {hp}\n- **Base HP:** {base_stats['base_hp']}\n**Possible Level and IV combinations:**\n"
        desc = top_line + (
            "\n".join(
                f" > - Level {lvl}: Possible IVs {ivs}" for lvl, ivs in possible.items()
            )
            or "No possible levels found with the given HP."
        )

        debug_log("Building embed and preparing response.")
        display_name = get_display_name(pokemon, dex=True)
        debug_log(f"Display name resolved: {display_name}")
        # desc is already set above; do not overwrite it
        # Embed the result
        embed = discord.Embed(
            title=f"Level and IV Estimation",
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

    find_level.extras = {"category": "Public"}


async def setup(bot):
    await bot.add_cog(FindLevel(bot))
