from utils.logs.pretty_log import pretty_log


# 💠────────────────────────────────────────────
# [📜 FETCH] All Straymons Members
# 💠────────────────────────────────────────────
async def fetch_all_straymon_members(bot):
    """
    Fetch all Straymons members from the database.
    Returns a list of asyncpg.Record objects, or an empty list if none found.
    """
    try:
        async with bot.pg_pool.acquire() as conn:
            rows = await conn.fetch("SELECT * FROM straymons_members ORDER BY user_id;")

        # 🩵 Log + Return

        pretty_log(
            "db",
            f"Fetched {len(rows)} straymons_members.",
        )
        return rows

    except Exception as e:

        pretty_log(
            "error",
            f"Failed to fetch straymons_members: {e}",
        )

async def update_patreon_status(bot, user_id: int, is_patreon: bool):
    """
    Update the Patreon status of a Straymon member in the database.
    """
    try:
        async with bot.pg_pool.acquire() as conn:
            await conn.execute(
                """
                UPDATE straymons_members
                SET is_patreon = $1
                WHERE user_id = $2;
                """,
                is_patreon,
                user_id,
            )
        pretty_log(
            "db",
            f"Updated Patreon status for user_id {user_id} to {is_patreon}.",
        )
        # Update the cache as well
        from utils.cache.straymon_member_cache import update_patreon_status_in_cache
        update_patreon_status_in_cache(user_id, is_patreon)

    except Exception as e:
        pretty_log(
            "error",
            f"Failed to update Patreon status for user_id {user_id}: {e}",
        )


async def update_catch_rate(bot, user_id: int, catch_rate_bonus: int):
    """
    Update the catch rate of a Straymon member in the database.
    """
    try:
        async with bot.pg_pool.acquire() as conn:
            await conn.execute(
                """
                UPDATE straymons_members
                SET catch_rate_bonus = $1
                WHERE user_id = $2;
                """,
                catch_rate_bonus,
                user_id,
            )
        pretty_log(
            "db",
            f"Updated catch rate for user_id {user_id} to {catch_rate_bonus}.",
        )
        from utils.cache.straymon_member_cache import update_catch_rate_in_cache
        update_catch_rate_in_cache(user_id, catch_rate_bonus)

    except Exception as e:
        pretty_log(
            "error",
            f"Failed to update catch rate for user_id {user_id}: {e}",
        )
