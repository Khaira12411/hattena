import discord

from utils.logs.pretty_log import pretty_log

# SQL SCRIPT
"""CREATE TABLE abilities (
    name TEXT PRIMARY KEY,
    description TEXT,
    standard TEXT[],
    secondary TEXT[],
    hidden TEXT[]
);"""

async def upsert_ability(
    bot: discord.Client,
    name: str,
    description: str,
    standard: list[str],
    secondary: list[str],
    hidden: list[str],
):
    try:
        async with bot.pg_pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO abilities (name, description, standard, secondary, hidden)
                VALUES ($1, $2, $3, $4, $5)
                ON CONFLICT (name) DO UPDATE
                SET description = EXCLUDED.description,
                    standard = EXCLUDED.standard,
                    secondary = EXCLUDED.secondary,
                    hidden = EXCLUDED.hidden;
                """,
                name,
                description,
                standard,
                secondary,
                hidden,
            )
            pretty_log(
                tag="db",
                message=f"Upserted ability '{name}' into database",
            )
            # Also update the cache
            from utils.cache.abilities_cache import upsert_ability_cache
            upsert_ability_cache(
                name,
                description,
                standard,
                secondary,
                hidden,
            )
    except Exception as e:
        pretty_log(
            tag="warn",
            message=f"⚠️ Failed to upsert ability '{name}' into database: {e}",
            exc=e,
        )

async def fetch_all_abilities(bot: discord.Client) -> list[dict]:
    try:
        async with bot.pg_pool.acquire() as conn:
            rows = await conn.fetch("SELECT * FROM abilities;")
            abilities = []
            for row in rows:
                abilities.append(
                    {
                        "name": row["name"],
                        "description": row["description"],
                        "standard": row["standard"],
                        "secondary": row["secondary"],
                        "hidden": row["hidden"],
                    }
                )
            pretty_log(
                tag="db",
                message=f"Fetched {len(abilities)} abilities from database",
            )
            return abilities
    except Exception as e:
        pretty_log(
            tag="warn",
            message=f"⚠️ Failed to fetch abilities from database: {e}",
            exc=e,
        )
        return []