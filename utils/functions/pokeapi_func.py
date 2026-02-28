import aiohttp
import discord

from utils.cache.market_value_cache import (
    fetch_pokemon_base_stats_cache,
    fetch_pokemon_weight_cache,
)
from utils.db.market_value_db import update_pokemon_stats
from utils.functions.pokemon_func import format_names_for_market_value_lookup
from utils.logs.debug_log import debug_enabled, debug_log, enable_debug
from utils.logs.pretty_log import pretty_log

#enable_debug(f"{__name__}.get_pokemon_stats")
#enable_debug(f"{__name__}.fetch_pokemon_base_stats_cache")
enable_debug(f"{__name__}.get_pokemon_weight")
#enable_debug(f"{__name__}.fetch_pokemon_stats_from_api")
enable_debug(f"{__name__}.fetch_pokemon_weight_from_api")
enable_debug(f"{__name__}.format_name_for_api_lookup")


def get_base_name(pokemon_name: str) -> str:
    """Extract the base name of a Pokémon, removing prefixes like 'Shiny' or 'Golden'."""
    for prefix in ["shiny ", "golden "]:
        if pokemon_name.lower().startswith(prefix):
            return pokemon_name[len(prefix) :].strip()
    return pokemon_name.strip()


async def get_pokemon_stats(
    bot: discord.Client, name: str, is_golden: bool = False
) -> dict | None:
    debug_log(f"get_pokemon_stats called with name={name}, is_golden={is_golden}")
    # Try cache first

    cache_name = format_names_for_market_value_lookup(name)
    debug_log(f"Cache lookup name: {cache_name}")
    stats = fetch_pokemon_base_stats_cache(cache_name)
    if stats and all(v is not None for v in stats.values()):
        debug_log(f"Stats found in cache: {stats}")

        return stats
    # Fallback to get base form stats and then adjust for golden if needed
    if is_golden:
        base_name = get_base_name(name)
        debug_log(f"Base name for golden Pokémon: {base_name}")
        base_cache_name = format_names_for_market_value_lookup(base_name)
        debug_log(f"Cache lookup name for base form: {base_cache_name}")
        base_stats = fetch_pokemon_base_stats_cache(base_cache_name)
        if base_stats and all(v is not None for v in base_stats.values()):
            debug_log(f"Base stats found in cache for golden Pokémon: {base_stats}")
            # Add 15 to all base stats for golden Pokémon
            adjusted_stats = {
                "base_hp": base_stats.get("base_hp", 0) + 15,
                "base_atk": base_stats.get("base_atk", 0) + 15,
                "base_spe": base_stats.get("base_spe", 0) + 15,
                "base_spa": base_stats.get("base_spa", 0) + 15,
                "base_def": base_stats.get("base_def", 0) + 15,
                "base_spd": base_stats.get("base_spd", 0) + 15,
                "ability": base_stats.get("ability"),
            }
            debug_log(f"Adjusted stats for golden Pokémon: {adjusted_stats}")
            await update_pokemon_stats(
                bot=bot,
                pokemon_name=cache_name,
                base_atk=adjusted_stats["base_atk"],
                base_def=adjusted_stats["base_def"],
                base_hp=adjusted_stats["base_hp"],
                base_spa=adjusted_stats["base_spa"],
                base_spd=adjusted_stats["base_spd"],
                base_spe=adjusted_stats["base_spe"],
                ability=adjusted_stats["ability"],
            )
            return adjusted_stats
        else:
            debug_log(
                f"Base stats not found in cache for golden Pokémon: {base_cache_name}"
            )

    # Fallback to API if not in cache or cache is invalid
    debug_log(f"Stats not found in cache or cache is invalid, fetching from API.")
    stats = await fetch_pokemon_stats_from_api(name, is_golden=is_golden)
    if stats and all(v is not None for v in stats.values()):
        debug_log(f"Stats fetched from API: {stats}")
        await update_pokemon_stats(
            bot=bot,
            pokemon_name=cache_name,
            base_atk=stats["base_atk"],
            base_def=stats["base_def"],
            base_hp=stats["base_hp"],
            base_spa=stats["base_spa"],
            base_spd=stats["base_spd"],
            base_spe=stats["base_spe"],
            ability=stats["ability"],
        )
        return stats
    else:
        debug_log(f"Failed to fetch valid stats from API for {name}")


async def get_pokemon_weight(name: str) -> str | None:
    # Try cache first
    cache_name = format_names_for_market_value_lookup(name)
    debug_log(f"Cache lookup name: {cache_name}")
    weight = fetch_pokemon_weight_cache(cache_name)
    if weight is not None:
        debug_log(f"Weight found in cache: {weight}")
        return weight
    # Fallback to API if not in cache
    debug_log(f"Weight not found in cache, fetching from API.")
    return await fetch_pokemon_weight_from_api(name)


async def fetch_pokemon_stats_from_api(
    name: str, is_golden: bool = False
) -> dict | None:
    debug_log(
        f"fetch_pokemon_stats_from_api called with name={name}, is_golden={is_golden}"
    )
    # Remove Golden prefix for API lookup, but keep it for display formatting
    look_up_name = name.lower().replace("golden ", "").replace("golden", "").strip()
    debug_log(f"API lookup name: {look_up_name}")
    url_name = format_name_for_api_lookup(look_up_name)
    url = f"https://pokeapi.co/api/v2/pokemon/{url_name}"
    debug_log(f"API URL: {url}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                debug_log(f"API response status: {resp.status}")
                if resp.status != 200:
                    debug_log(f"API response status not 200: {resp.status}")
                    return None
                data = await resp.json()
        # debug_log(f"API response data: {data}")
        stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
        debug_log(f"Parsed stats: {stats}")
        abilities = [a["ability"]["name"] for a in data["abilities"]]
        debug_log(f"Parsed abilities: {abilities}")
        # If is_golden, add 15 to all base stats
        if is_golden:
            debug_log("Adding 15 to all base stats for golden Pokémon.")
            stats["attack"] = stats.get("attack", 0) + 15
            stats["speed"] = stats.get("speed", 0) + 15
            stats["special-attack"] = stats.get("special-attack", 0) + 15
            stats["defense"] = stats.get("defense", 0) + 15
            stats["special-defense"] = stats.get("special-defense", 0) + 15
        return {
            "base_hp": stats.get("hp"),
            "base_atk": stats.get("attack"),
            "base_spe": stats.get("speed"),
            "base_spa": stats.get("special-attack"),
            "base_def": stats.get("defense"),
            "base_spd": stats.get("special-defense"),
            "ability": ",".join(abilities),
        }
    except Exception as e:
        debug_log(f"Exception in fetch_pokemon_stats_from_api: {e}")
        return None


async def fetch_pokemon_weight_from_api(name: str) -> dict | None:
    debug_log(f"fetch_pokemon_weight_from_api called with name={name}")
    look_up_name = name.lower().replace("golden ", "").replace("golden", "").strip()
    debug_log(f"API lookup name: {look_up_name}")
    url_name = format_name_for_api_lookup(look_up_name)
    url = f"https://pokeapi.co/api/v2/pokemon/{url_name}"
    debug_log(f"API URL: {url}")
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                debug_log(f"API response status: {resp.status}")
                if resp.status != 200:
                    debug_log(f"API response status not 200: {resp.status}")
                    return None
                data = await resp.json()
        # debug_log(f"API response data: {data}")
        weight = data.get("weight")
        debug_log(f"Parsed weight: {weight}")
        if weight is not None:
            return str(weight)
        return None
    except Exception as e:
        debug_log(f"Exception in fetch_pokemon_weight_from_api: {e}")
        return None


def format_name_for_api_lookup(name: str) -> str:
    debug_log(f"format_name_for_api_lookup called with name={name}")
    name = name.lower().replace(" ", "-")
    # Handle Mega, Primal, Alolan, Galarian, Hisuian, etc.
    special_forms = [
        "mega",
        "primal",
        "alola",
        "galar",
        "hisui",
        "paldea",
        "gigantamax",
        "totem",
        "origin",
        "eternamax",
        "starter",
    ]
    # Handle Mega Mewtwo X/Y and similar forms
    # e.g., mega-mewtwo-x or mega-mewtwo-y or mega mewtwo x
    if name.startswith("mega-mewtwo-") and (name.endswith("-x") or name.endswith("-y")):
        letter = name[-1]
        return f"mewtwo-mega-{letter}"
    # General special forms
    for form in special_forms:
        if name.startswith(form + "-"):
            rest = name[len(form) + 1 :]
            # Check for trailing -x or -y (for other possible forms)
            if rest.endswith("-x") or rest.endswith("-y"):
                base = rest[:-2]
                letter = rest[-1]
                return f"{base}-{form}-{letter}"
            return f"{rest}-{form}"
        if name.endswith("-" + form):
            # already in correct format
            return name
        # e.g., mewtwo-mega-x or mewtwo-mega-y
        if name.endswith("-" + form + "-x") or name.endswith("-" + form + "-y"):
            return name
    return name
