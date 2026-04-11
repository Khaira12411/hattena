from datetime import datetime

import discord

from utils.cache.cache_list import market_value_cache
from utils.logs.pretty_log import pretty_log

def get_pokemon_names_cache():
    """
    Get a list of all Pokémon names currently in the market value cache.
    """
    return list(market_value_cache.keys())

# 💠────────────────────────────────────────────
# [📜 UPDATE] Market Value Cache for a Pokémon
# 💠────────────────────────────────────────────
def update_pokemon_stats_cache(pokemon_name: str, pokemon_data: dict):
    """
    Update the market value cache for a specific Pokémon.
    pokemon_data should contain keys like:
    - rarity
    - emoji_id
    - base_atk
    - base_def
    - base_hp
    - base_spa
    - base_spd
    - base_spe
    - weight
    - ability
    """
    if pokemon_name.lower() in market_value_cache:
        market_value_cache[pokemon_name.lower()].update(pokemon_data)

def update_rarity_cache(pokemon_name: str, rarity: str):
    if pokemon_name in market_value_cache:
        market_value_cache[pokemon_name]["rarity"] = rarity

def update_dex_number_cache(pokemon_name: str, dex_number: int):
    if pokemon_name in market_value_cache:
        market_value_cache[pokemon_name]["dex_number"] = dex_number

# 💠────────────────────────────────────────────
# [📜 FETCH] Market Value Data for a Pokémon
# 💠────────────────────────────────────────────
def fetch_pokemon_base_stats_cache(pokemon_name: str):
    """
    Get base stats for a specific Pokémon from cache.
    Returns dict with base stats or None if not found.
    """
    pokemon_data = market_value_cache.get(pokemon_name.lower())
    if pokemon_data:
        return {
            "base_atk": pokemon_data.get("base_atk"),
            "base_def": pokemon_data.get("base_def"),
            "base_hp": pokemon_data.get("base_hp"),
            "base_spa": pokemon_data.get("base_spa"),
            "base_spd": pokemon_data.get("base_spd"),
            "base_spe": pokemon_data.get("base_spe"),
        }
    return None

def fetch_pokemon_weight_cache(pokemon_name: str):
    """
    Get weight for a specific Pokémon from cache.
    Returns weight or None if not found.
    """
    pokemon_data = market_value_cache.get(pokemon_name.lower())
    if pokemon_data:
        return pokemon_data.get("weight")
    return None

def fetch_market_value_cache(pokemon_name: str):
    """
    Get market value data for a specific Pokémon from cache.
    Returns dict with market data or None if not found.
    """
    return market_value_cache.get(pokemon_name.lower())


def fetch_lowest_market_value_cache(pokemon_name: str):
    """
    Get lowest market value for a Pokémon from cache.
    Returns 0 if not found or no data.
    """
    pokemon_data = market_value_cache.get(pokemon_name.lower())
    if pokemon_data:
        return pokemon_data.get("lowest_market", 0)
    return 0


def fetch_pokemon_exclusivity_cache(pokemon_name: str):
    """
    Get exclusivity status for a Pokémon from cache.
    Returns False if not found or no data.
    """
    pokemon_data = market_value_cache.get(pokemon_name.lower())
    if pokemon_data:
        return pokemon_data.get("is_exclusive", False)
    return False


def fetch_emoji_id_cache(pokemon_name: str):
    """
    Get emoji ID for a Pokémon from cache.
    Returns 0 if not found or no data.
    """
    pokemon_data = market_value_cache.get(pokemon_name.lower())
    if pokemon_data:
        return pokemon_data.get("emoji_id", 0)
    return None

def fetch_pokemon_exclusivity_cache(pokemon_name: str):
    """
    Get exclusivity status for a Pokémon from cache.
    Returns False if not found or no data.
    """
    pokemon_data = market_value_cache.get(pokemon_name.lower())
    if pokemon_data:
        return pokemon_data.get("is_exclusive", False)
    return False


def fetch_rarity_cache(pokemon_name: str):
    """
    Get rarity for a Pokémon from cache.
    Returns 'unknown' if not found or no data.
    """
    pokemon_data = market_value_cache.get(pokemon_name.lower())
    if pokemon_data:
        return pokemon_data.get("rarity", "unknown")
    return "unknown"


def fetch_dex_number_cache(pokemon_name: str):
    """
    Get dex number for a Pokémon from cache.
    Returns 0 if not found or no data.
    """
    pokemon_data = market_value_cache.get(pokemon_name.lower())
    if pokemon_data:
        return pokemon_data.get("dex_number", 0)
    return 0


def is_pokemon_exclusive_cache(pokemon_name: str):
    """
    Check if a Pokémon is exclusive based on cache data.
    Returns False if not found or no data.
    """
    pokemon_data = market_value_cache.get(pokemon_name.lower())
    if pokemon_data:
        return pokemon_data.get("is_exclusive", False)
    return False


def fetch_image_link_cache(pokemon_name: str):
    """
    Get image link for a Pokémon from cache.
    Returns None if not found or no data.
    """
    pokemon_data = market_value_cache.get(pokemon_name.lower())
    if pokemon_data:
        return pokemon_data.get("image_link", None)
    return None

def fetch_pokemon_name_by_dex_cache(dex_number: int):
    """
    Get Pokémon name by dex number from cache.
    Returns None if not found or no data.
    """
    for name, data in market_value_cache.items():
        if data.get("dex_number") == dex_number:
            return name
    return None