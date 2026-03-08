import discord
from discord import app_commands

from utils.logs.pretty_log import pretty_log

# SQL SCRIPT
"""CREATE TABLE straydex_guilds (
    guild_id BIGINT PRIMARY KEY,
    guild_name TEXT,
    update_channel_id BIGINT,
    update_channel_name TEXT
);"""


async def upsert_straydex_guild(
    bot,
    guild_id: int,
    guild_name: str,
    update_channel_id: int = None,
    update_channel_name: str = None,
):
    """
    Insert or update a Straydex guild record in the database.
    """
    try:
        async with bot.pg_pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO straydex_guilds (guild_id, guild_name, update_channel_id, update_channel_name)
                VALUES ($1, $2, $3, $4)
                ON CONFLICT (guild_id) DO UPDATE
                SET guild_name = EXCLUDED.guild_name,
                    update_channel_id = EXCLUDED.update_channel_id,
                    update_channel_name = EXCLUDED.update_channel_name;
                """,
                guild_id,
                guild_name,
                update_channel_id,
                update_channel_name,
            )
        pretty_log(
            "db",
            f"Upserted Straydex guild {guild_name} (ID: {guild_id}) with update channel {update_channel_name} (ID: {update_channel_id}).",
        )
        from utils.cache.straydex_guild_cache import upsert_straydex_guild_cache
        upsert_straydex_guild_cache(guild_id, guild_name, update_channel_id, update_channel_name)
    except Exception as e:
        pretty_log(
            "error",
            f"Failed to upsert Straydex guild {guild_name} (ID: {guild_id}): {e}",
        )


async def remove_straydex_guild(bot, guild_id: int):
    """
    Remove a Straydex guild record from the database.
    """
    try:
        async with bot.pg_pool.acquire() as conn:
            await conn.execute(
                """
                DELETE FROM straydex_guilds
                WHERE guild_id = $1;
                """,
                guild_id,
            )
        pretty_log(
            "db",
            f"Removed Straydex guild with ID: {guild_id}.",
        )
        from utils.cache.straydex_guild_cache import remove_straydex_guild_cache
        remove_straydex_guild_cache(guild_id)
    except Exception as e:
        pretty_log(
            "error",
            f"Failed to remove Straydex guild with ID: {guild_id}: {e}",
        )


async def get_all_straydex_guilds(bot):
    """
    Retrieve all Straydex guild records from the database.
    """
    try:
        async with bot.pg_pool.acquire() as conn:
            rows = await conn.fetch(
                """
                SELECT guild_id, guild_name, update_channel_id, update_channel_name
                FROM straydex_guilds;
                """
            )
        guilds = [
            {
                "guild_id": row["guild_id"],
                "guild_name": row["guild_name"],
                "update_channel_id": row["update_channel_id"],
                "update_channel_name": row["update_channel_name"],
            }
            for row in rows
        ]
        pretty_log(
            "db",
            f"Retrieved {len(guilds)} Straydex guild(s) from the database.",
        )
        return guilds
    except Exception as e:
        pretty_log(
            "error",
            f"Failed to retrieve Straydex guilds from the database: {e}",
        )
        return []
