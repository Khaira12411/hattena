# --------------------
#  Market embed parser utility
# --------------------
import re
from typing import Optional, Tuple

import discord

from utils.cache.market_value_cache import (
    fetch_dex_number_cache,
    fetch_emoji_id_cache,
    fetch_image_link_cache,
    fetch_market_value_cache,
    fetch_pokemon_exclusivity_cache,
    fetch_rarity_cache,
)
from utils.db.market_value_db import (
    update_dex_number,
    update_emoji_id,
    update_is_exclusive,
    update_pokemon_stats,
    update_rarity,
    upsert_image_link,
)
from utils.functions.pokemon_func import (
    format_names_for_market_value_lookup,
    is_mon_exclusive,
)
from utils.logs.debug_log import debug_enabled, debug_log, enable_debug
from utils.logs.pretty_log import pretty_log

#enable_debug(f"{__name__}.dex_listener")
#enable_debug(f"{__name__}.parse_stats_and_abilities_from_embed_and_update")
# enable_debug(f"{__name__}.extract_emoji_id_from_evolution_line")
# enable_debug(f"{__name__}.extract_rarity_from_embed")
emoji_map = {
    "common": "common",
    "uncommon": "uncommon",
    "rare": "rare",
    "superrare": "superrare",
    "legendary": "legendary",
    "shiny": "shiny",
    "golden": "golden",
    "shinymega": "shiny mega",
    "shinygigantamax": "shiny gigantamax",
    "mega": "mega",
    "gigantamax": "gigantamax",
    "goldenmega": "golden mega",
    "goldengigantamax": "golden gigantamax",
}


async def parse_stats_and_abilities_from_embed_and_update(
    bot: discord.Client, embed, pokemon_name
) -> dict:
    """
    Parses base stats and abilities from a Discord embed object.
    Returns a dict with base stats and a list of abilities.
    """
    stats = {}
    debug_log(f"Parsing stats and abilities for {pokemon_name} from embed: {embed}")
    # Combine all field values into one string for easier regex search
    fields_text = ""
    for field in embed.fields:
        debug_log(f"Embed field: name={field.name}, value={field.value}")
        fields_text += f"{field.name}: {field.value}\n"
    debug_log(f"Combined fields_text for {pokemon_name}: {fields_text!r}")

    # Regex patterns for each stat
    patterns = {
        "base_atk": r"Base Attack.*?:crossed_swords: (\d+)",
        "base_def": r"Base Defense.*?:shield: (\d+)",
        "base_hp": r"Base HP.*?:sparkling_heart: (\d+)",
        "base_spa": r"Base Sp\. Atk.*?:boom: (\d+)",
        "base_spd": r"Base Sp\. Def.*?:beginner: (\d+)",
        "base_spe": r"Base Speed.*?:zap: (\d+)",
    }
    for key, pat in patterns.items():
        debug_log(f"Searching for {key} with pattern {pat!r} in fields_text.")
        match = re.search(pat, fields_text)
        if match:
            stats[key] = int(match.group(1))
            debug_log(f"Found {key}: {stats[key]}")
        else:
            debug_log(
                f"Did not find {key} in fields_text. Pattern used: {pat!r}. Example fields_text: {fields_text}"
            )

    # Abilities block
    abilities_match = re.search(
        r"Abilities.*?:\s*([\s\S]+?)(?=\n\w.*?:|$)", fields_text
    )
    debug_log(f"Abilities regex match object for {pokemon_name}: {abilities_match}")
    if abilities_match:
        debug_log(f"Abilities block found: {abilities_match.group(1)!r}")
        # Split abilities by line, remove formatting
        abilities = [
            re.sub(r"\s*\\*\\(.*?\\)\\*", "", line).strip()
            for line in abilities_match.group(1).splitlines()
            if line.strip()
        ]
        stats["abilities"] = abilities
        debug_log(f"Parsed abilities: {abilities}")
    else:
        debug_log(f"No abilities block found in fields_text for {pokemon_name}.")

    # (emoji_id extraction removed as requested)
    debug_log(f"Final parsed stats dict: {stats}")
    if stats:
        # Get old value
        formatted_name = format_names_for_market_value_lookup(pokemon_name)
        old_data = fetch_market_value_cache(formatted_name) or {}
        debug_log(f"Old data from cache for {formatted_name}: {old_data}")
        stat_keys = [
            "base_atk",
            "base_def",
            "base_hp",
            "base_spa",
            "base_spd",
            "base_spe",
        ]
        stat_diff = any(stats.get(key) != old_data.get(key) for key in stat_keys)
        abilities_diff = stats.get("abilities") != old_data.get("ability", "").split(
            ","
        )
        emoji_id_diff = stats.get("emoji_id") != old_data.get("emoji_id")
        debug_log(
            f"Stat diff: {stat_diff}, Abilities diff: {abilities_diff}, Emoji ID diff: {emoji_id_diff}"
        )
        if stat_diff or abilities_diff or emoji_id_diff:
            debug_log(f"Updating stats for {pokemon_name} with {stats}")
            try:
                await update_pokemon_stats(
                    bot,
                    pokemon_name,
                    base_atk=stats.get("base_atk"),
                    base_def=stats.get("base_def"),
                    base_hp=stats.get("base_hp"),
                    base_spa=stats.get("base_spa"),
                    base_spd=stats.get("base_spd"),
                    base_spe=stats.get("base_spe"),
                    ability=",".join(stats.get("abilities", [])),
                )
                debug_log(f"Successfully updated stats for {pokemon_name}.")
            except Exception as e:
                debug_log(
                    f"Failed to update stats for {pokemon_name} with {stats}: {e}",
                    exc=e,
                )
                pretty_log(
                    "warn",
                    f"⚠️ Failed to update stats for {pokemon_name} with {stats}: {e}",
                    exc=e,
                )
        else:
            debug_log(
                f"No update needed for {pokemon_name}. Stats, abilities, and emoji_id match cache."
            )
    return stats


def extract_pokemon_name_and_dex(text):
    match = re.match(r"(.+?)\s*#(\d+)", text)
    if match:
        name = match.group(1).strip()
        dex = match.group(2).strip()
        return name, dex
    else:
        return text.strip(), None


def extract_rarity_from_embed(embed) -> str:
    """
    Extracts the rarity text or emoji name from the 'Rarity' field in a Discord embed object.
    Returns the mapped rarity as a string (e.g., 'shiny gigantamax').
    """
    debug_log("Starting rarity extraction from embed.")
    fields = []
    # Try to get fields from embed object (discord.py Embed or dict)
    if hasattr(embed, "fields"):
        fields = embed.fields
        debug_log(f"Embed fields attribute found: {fields}")
    elif isinstance(embed, dict) and "fields" in embed:
        fields = embed["fields"]
        debug_log(f"Embed fields key found: {fields}")
    else:
        debug_log(f"Embed has no fields attribute or key. Embed: {embed}")
    for idx, field in enumerate(fields):
        debug_log(f"Checking field {idx}: {field}")
        name = (
            field.get("name")
            if isinstance(field, dict)
            else getattr(field, "name", None)
        )
        value = (
            field.get("value")
            if isinstance(field, dict)
            else getattr(field, "value", None)
        )
        debug_log(f"Field name: {name}, value: {value}")
        if name and name.lower() == "rarity":
            debug_log(f"Found 'Rarity' field with value: {value}")
            match = re.search(r"<:([a-zA-Z0-9_]+):[0-9]+>", value)
            if match:
                emoji_name = match.group(1)
                debug_log(f"Extracted emoji name: {emoji_name}")
                mapped_rarity = emoji_map.get(emoji_name.lower(), emoji_name)
                debug_log(f"Mapped rarity: {mapped_rarity}")
                return mapped_rarity
            debug_log(f"Returning plain rarity value: {value.strip()}")
            return value.strip()
    debug_log("'Rarity' field not found in embed.")
    return ""


async def dex_listener(bot, message: discord.Message):
    """Listens to dex command and updates the image link in the market value cache if it differs from the one in the command output."""
    embed = message.embeds[0] if message.embeds else None
    if not embed:
        return

    embed_title = embed.title if embed.title else ""
    embed_author_name = embed.author.name if embed.author else ""
    pokemon_name, dex_number = extract_pokemon_name_and_dex(embed_author_name)
    if not pokemon_name:
        debug_log(
            f"Could not extract pokemon name from embed title: '{embed_author_name}'"
        )
        return
    pokemon_name = format_names_for_market_value_lookup(pokemon_name)
    embed_image_url = embed.image.url if embed.image else None
    image_link_cache = fetch_image_link_cache(pokemon_name)
    existing_exclusive_status = fetch_pokemon_exclusivity_cache(pokemon_name)
    is_exclusive = is_mon_exclusive(pokemon_name)
    if existing_exclusive_status != is_exclusive and is_exclusive == False:
        new_exclusive = is_exclusive
        await update_is_exclusive(bot, pokemon_name, new_exclusive)
    else:
        new_exclusive = existing_exclusive_status
    if embed_image_url and image_link_cache != embed_image_url:
        await upsert_image_link(bot, pokemon_name, embed_image_url, new_exclusive)
        debug_log(f"Updated image link for {pokemon_name} to {embed_image_url}.")
        pretty_log(
            "info",
            f"Updated image link for {pokemon_name} to {embed_image_url}.",
        )
    old_dex_number = fetch_dex_number_cache(pokemon_name)
    if dex_number and str(old_dex_number) != str(dex_number):
        dex_number = int(dex_number)
        await update_dex_number(bot, pokemon_name, dex_number)
        debug_log(f"Updated dex number for {pokemon_name} to {dex_number}.")

    old_rarity = fetch_rarity_cache(pokemon_name)
    rarity = extract_rarity_from_embed(embed)

    if rarity and old_rarity != rarity:
        await update_rarity(bot, pokemon_name, rarity)
        debug_log(f"Updated rarity for {pokemon_name} to {rarity}.")


    old_emoji_id = fetch_emoji_id_cache(pokemon_name)
    if not old_emoji_id:
        emoji_id = extract_emoji_id_from_evolution_line(embed.description or "")
        if emoji_id and old_emoji_id != emoji_id:
            try:
                await update_emoji_id(bot, pokemon_name, emoji_id)
                debug_log(f"Updated emoji ID for {pokemon_name} to {emoji_id}.")
            except Exception as e:
                pretty_log(
                    "warn",
                    f"⚠️ Failed to update emoji ID for {pokemon_name} to {emoji_id}: {e}",
                    exc=e,
                )

    try:

        await parse_stats_and_abilities_from_embed_and_update(bot, embed, pokemon_name)
    except Exception as e:
        debug_log(
            f"Failed to parse stats and abilities for {pokemon_name} from embed: {e}",
            exc=e,
        )
        pretty_log(
            "warn",
            f"⚠️ Failed to parse stats and abilities for {pokemon_name} from embed: {e}",
            exc=e,
        )


def extract_emoji_id_from_evolution_line(description: str) -> str | None:
    """
    Extracts the first emoji tag before any bolded Pokémon name in the evolution line from a description string.
    Returns the emoji tag as a string, or None if not found.
    """
    debug_log(f"Extracting emoji tag from description: {description!r}")
    # Find the evolution line section
    evo_line_match = re.search(
        r":dna: \*\*Evolution line\*\*\s*\n([^\n]+)", description
    )
    if evo_line_match:
        evo_line = evo_line_match.group(1)
        debug_log(f"Evolution line found: {evo_line!r}")
        # Now extract the emoji tag before the bolded name
        emoji_match = re.search(r"(<:[^:]+:\d+>) \*\*.+?\*\*", evo_line)
        if emoji_match:
            emoji_tag = emoji_match.group(1)
            debug_log(f"Found emoji tag: {emoji_tag}")
            return emoji_tag
        debug_log("No emoji tag found in evolution line.")
    else:
        debug_log("No evolution line found in description.")
    return None
