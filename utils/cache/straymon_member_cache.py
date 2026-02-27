import time

import discord

from utils.cache.cache_list import straymon_member_cache
from utils.logs.pretty_log import pretty_log
from utils.db.straymon_db import fetch_all_straymon_members

async def load_straymon_member_cache(bot):
    """
    Load all straymon members into memory cache.
    Uses the fetch_all_straymon_members DB function.
    """

    straymon_member_cache.clear()
    rows = await fetch_all_straymon_members(bot)
    for row in rows:
        straymon_member_cache[row["user_id"]] = {
            "user_name": row.get("user_name"),
            "channel_id": row.get("channel_id"),
            "faction": row.get("faction"),
            "catch_rate_bonus": row.get("catch_rate_bonus"),
            "is_patreon": row.get("is_patreon"),
        }

    try:
        pretty_log(
            "info",
            f"Loaded {len(straymon_member_cache)} straymon members into cache",
            label="💠 STRAYMON MEMBER CACHE",
            bot=bot,
        )
    except Exception as e:
        # fallback to console if Discord logging fails
        print(
            f"[💠 STRAYMON MEMBER CACHE] Loaded {len(straymon_member_cache)} entries (pretty_log failed: {e})"
        )

    return straymon_member_cache


def fetch_straymon_member_cache(user_id: int):
    """
    Fetch a straymon member from cache by user ID.
    Returns a dict with user_name and channel_id, or None if not found.
    """
    return straymon_member_cache.get(user_id)


def fetch_straymon_member_cache_by_name(user_name: str) -> dict | None:
    """
    Fetch a member's info from the Straymon cache by their user_name.
    Strips whitespace and compares case-insensitively.
    """
    if not user_name:
        return None

    lowered_name = user_name.strip().lower()

    for user_id, data in straymon_member_cache.items():
        if not data or not isinstance(data, dict):
            continue

        cached_user_name = data.get("user_name")
        if cached_user_name and str(cached_user_name).strip().lower() == lowered_name:
            return data

    return None


def fetch_straymon_member_cache_by_username(user_name: str) -> tuple[int, dict] | None:
    """
    Fetch a member's info and user_id from the Straymon cache by their user_name.
    Strips whitespace and compares case-insensitively.
    """
    if not user_name:
        return None

    lowered_name = user_name.strip().lower()

    for user_id, data in straymon_member_cache.items():
        if not data or not isinstance(data, dict):
            continue

        cached_user_name = data.get("user_name")
        if cached_user_name and str(cached_user_name).strip().lower() == lowered_name:
            return user_id, data

    return None


def fetch_straymon_user_id_by_username(user_name: str) -> int | None:
    """
    Fetch a member's user_id from the Straymon cache by their user_name.
    Strips whitespace and compares case-insensitively.
    """
    if not user_name:
        return None

    lowered_name = user_name.strip().lower()

    for user_id, data in straymon_member_cache.items():
        if not data or not isinstance(data, dict):
            continue

        cached_user_name = data.get("user_name")
        if cached_user_name and str(cached_user_name).strip().lower() == lowered_name:
            return user_id

    return None


def update_catch_rate_in_cache(user_id: int, catch_rate_bonus: int):
    """
    Update the catch rate of a Straymon member in the cache.
    """
    if user_id in straymon_member_cache:
        if isinstance(straymon_member_cache[user_id], dict):
            straymon_member_cache[user_id]["catch_rate_bonus"] = catch_rate_bonus


def update_patreon_status_in_cache(user_id: int, is_patreon: bool):
    """
    Update the Patreon status of a Straymon member in the cache.
    """
    if user_id in straymon_member_cache:
        if isinstance(straymon_member_cache[user_id], dict):
            straymon_member_cache[user_id]["is_patreon"] = is_patreon
