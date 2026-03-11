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

# Nature stat modifier map
NATURE_MAP = {
    "Adamant": {"up": "attack", "down": "special-attack"},
    "Brave": {"up": "attack", "down": "speed"},
    "Lonely": {"up": "attack", "down": "defense"},
    "Naughty": {"up": "attack", "down": "special-defense"},
    "Bold": {"up": "defense", "down": "attack"},
    "Impish": {"up": "defense", "down": "special-attack"},
    "Lax": {"up": "defense", "down": "special-defense"},
    "Relaxed": {"up": "defense", "down": "speed"},
    "Modest": {"up": "special-attack", "down": "attack"},
    "Mild": {"up": "special-attack", "down": "defense"},
    "Quiet": {"up": "special-attack", "down": "speed"},
    "Rash": {"up": "special-attack", "down": "special-defense"},
    "Calm": {"up": "special-defense", "down": "attack"},
    "Careful": {"up": "special-defense", "down": "special-attack"},
    "Gentle": {"up": "special-defense", "down": "defense"},
    "Sassy": {"up": "special-defense", "down": "speed"},
    "Hasty": {"up": "speed", "down": "defense"},
    "Jolly": {"up": "speed", "down": "special-attack"},
    "Naive": {"up": "speed", "down": "special-defense"},
    "Timid": {"up": "speed", "down": "attack"},
    # Neutral natures
    "Bashful": {"up": None, "down": None},
    "Docile": {"up": None, "down": None},
    "Hardy": {"up": None, "down": None},
    "Quirky": {"up": None, "down": None},
    "Serious": {"up": None, "down": None},
}

enable_debug(f"{__name__}.calculate_non_hp")
enable_debug(f"{__name__}.calculate_hp")
enable_debug(f"{__name__}.stats_calculator")


def calculate_non_hp(base_stat, iv, ev, lvl, stat_name, nature=None):
    """
    Calculate non-HP stat using the provided formula:
    stat = lvl/100 * (base_stat * 2.7 + iv + floor(ev/4)) + iv + 5
    Applies nature modifier if provided.
    Logs all intermediate values for debugging.
    """
    from math import floor

    pre_ev = base_stat * 2.7
    ev_floor = floor(ev / 4)
    pre_stat = pre_ev + iv + ev_floor
    stat_before_iv5 = (lvl / 100) * pre_stat
    stat_before_nature = stat_before_iv5 + iv + 5

    debug_log(
        f"[STAT DEBUG] base_stat*2.7={pre_ev}, floor(ev/4)={ev_floor}, pre_stat={pre_stat}, stat_before_iv5={stat_before_iv5}, stat_before_nature={stat_before_nature}"
    )

    # Floor before applying nature modifier (PokéMeow style)
    floored_before_nature = floor(stat_before_nature)
    debug_log(f"[STAT DEBUG] floored_before_nature={floored_before_nature}")

    # Apply nature modifier if nature is provided
    nature_mod = 1.0
    if nature and nature in NATURE_MAP:
        if NATURE_MAP[nature]["up"] == stat_name:
            nature_mod = 1.1  # 10% increase
        elif NATURE_MAP[nature]["down"] == stat_name:
            nature_mod = 0.9  # 10% decrease
    stat_after_nature = floored_before_nature * nature_mod
    debug_log(
        f"[STAT DEBUG] nature_mod={nature_mod}, stat_after_nature={stat_after_nature}"
    )

    final_stat = floor(stat_after_nature)
    debug_log(f"[STAT DEBUG] final_stat (floored)={final_stat}")
    return final_stat


def calculate_hp(base_hp, iv, ev, lvl):
    """
    Calculate HP stat using the provided formula:
    HP = lvl * [ (base_hp * 2.7 + iv + floor(ev/4)) / 100 + 1 ] + 10
    Rounds down ev/4 and the final result.
    """
    from math import floor

    hp = lvl * ((base_hp * 2.7 + iv + floor(ev / 4)) / 100 + 1) + 10
    return floor(hp)


async def nature_autocomplete(interaction: discord.Interaction, current: str):
    """
    Autocomplete for natures, showing up/down effect in the display.
    """
    results = []
    # Stat abbreviation mapping
    stat_abbr = {
        "attack": "Atk",
        "defense": "Def",
        "special-attack": "SpA",
        "special-defense": "SpD",
        "speed": "Spe",
    }
    for nature, effect in NATURE_MAP.items():
        up = effect["up"]
        down = effect["down"]
        if up and down:
            up_abbr = stat_abbr.get(up, up)
            down_abbr = stat_abbr.get(down, down)
            label = f"{nature} (+{up_abbr} -{down_abbr})"
        else:
            label = f"{nature} (neutral)"
        if current.lower() in nature.lower() or current.lower() in label.lower():
            results.append(app_commands.Choice(name=label, value=nature))
    # Show all if nothing typed, or filter if typed
    if not current:
        results = [
            app_commands.Choice(
                name=(
                    f"{nature} (+{stat_abbr.get(effect['up'], effect['up'])} -{stat_abbr.get(effect['down'], effect['down'])})"
                    if effect["up"] and effect["down"]
                    else f"{nature} (neutral)"
                ),
                value=nature,
            )
            for nature, effect in NATURE_MAP.items()
        ]
    return results[:25]  # Discord max


class StatsCalculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        debug_log("StatsCalculator cog initialized.")

    @app_commands.command(
        name="stats-calculator",
        description="Calculate Pokémon stats based on IVs, EVs, and level.",
    )
    @app_commands.autocomplete(pokemon=pokemon_autocomplete, nature=nature_autocomplete)
    @app_commands.describe(
        pokemon="The name of the Pokémon.",
        nature="The nature of the Pokémon",
        stat="The stat to calculate (hp, attack, defense, special-attack, special-defense, speed).",
        ivs="The Individual Values (IVs) for the stat.",
        evs="The Effort Values (EVs) for the stat.",
        level="The level of the Pokémon.",
    )
    async def stats_calculator(
        self,
        interaction: discord.Interaction,
        pokemon: str,
        nature: str,
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
                    base_stats[stat_key], ivs, evs, level, stat, nature
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
        display_name = get_display_name(pokemon, dex=True)
        debug_log(f"Display name resolved: {display_name}")
        # Nature effect details
        if nature in NATURE_MAP:
            up_stat = NATURE_MAP[nature]["up"]
            down_stat = NATURE_MAP[nature]["down"]
            if up_stat:
                up_str = f"{up_stat.replace('-', ' ').title()} (+10%)"
            else:
                up_str = "None"
            if down_stat:
                down_str = f"{down_stat.replace('-', ' ').title()} (-10%)"
            else:
                down_str = "None"
        else:
            up_str = down_str = "None"

        desc = (
            f"> - **Stat:** {stat.replace('-', ' ').title()}\n"
            f"> - **IVs:** {ivs}\n"
            f"> - **EVs:** {evs}\n"
            f"> - **Level:** {level}\n"
            f"> - **Nature:** {nature}\n"
            f"> - **Nature Effect:** Up: {up_str} | Down: {down_str}\n"
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

        pretty_log(
            "success",
            f"{interaction.user.name} used stats-calculator for {pokemon} - Stat: {stat}, IVs: {ivs}, EVs: {evs}, Level: {level}, Result: {calculated_stat}",
        )

    stats_calculator.extras = {"category": "Public"}


async def setup(bot):
    await bot.add_cog(StatsCalculator(bot))
