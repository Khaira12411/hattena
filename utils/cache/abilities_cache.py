import discord

from utils.db.abilities_db import fetch_all_abilities
from utils.logs.pretty_log import pretty_log

from .cache_list import abilities_cache


# 💫━━━━━━━━━━━━━━━━━━━━━━━━━
#       🌸 Abilities Cache 🌸
# 💫━━━━━━━━━━━━━━━━━━━━━━━━━
async def load_abilities_cache(bot: discord.Client):
    abilities_cache.clear()
    try:
        abilities = await fetch_all_abilities(bot)
        for ability in abilities:
            abilities_cache[ability["name"].lower()] = {
                "description": ability["description"],
                "standard": ability["standard"],
                "secondary": ability["secondary"],
                "hidden": ability["hidden"],
            }
        pretty_log(
            tag="cache",
            message=f"Loaded {len(abilities_cache)} abilities into cache",
        )
    except Exception as e:
        pretty_log(
            tag="warn",
            message=f"⚠️ Failed to load abilities cache from database: {e}",
            exc=e,
        )


def upsert_ability_cache(
    name: str,
    description: str,
    standard: list[str],
    secondary: list[str],
    hidden: list[str],
):
    abilities_cache[name.lower()] = {
        "description": description,
        "standard": standard,
        "secondary": secondary,
        "hidden": hidden,
    }
    pretty_log(
        tag="cache",
        message=f"Upserted ability '{name}' into cache",
    )


def get_ability_description(name: str) -> str | None:
    ability = abilities_cache.get(name.lower())
    if ability:
        return ability["description"]
    return None

def get_pokemons_with_ability(name: str) -> dict[str, list[str]] | None:
    ability = abilities_cache.get(name.lower())
    if ability:
        return {
            "standard": ability["standard"],
            "secondary": ability["secondary"],
            "hidden": ability["hidden"],
        }
    return None

def get_list_of_pokemons_with_ability(name: str) -> list[str] | None:
    ability = abilities_cache.get(name.lower())
    # Combine standard, secondary and hidden lists into one list
    if ability:
        return ability["standard"] + ability["secondary"] + ability["hidden"]
    return None

def check_ability_exists(name: str) -> bool:
    return name.lower() in abilities_cache