import discord

from utils.logs.pretty_log import pretty_log

# SQL SCRIPT
"""CREATE TABLE pokemon_moves (
    name TEXT PRIMARY KEY,
    learned_by TEXT[]
);"""

async def upsert_pokemon_moves(
    bot: discord.Client,
    name: str,
    learned_by: list[str],
):
    try:
        async with bot.pg_pool.acquire() as conn:
            await conn.execute(
                """
                INSERT INTO pokemon_moves (name, learned_by)
                VALUES ($1, $2)
                ON CONFLICT (name) DO UPDATE
                SET learned_by = EXCLUDED.learned_by;
                """,
                name,
                learned_by,
            )
            pretty_log(
                tag="db",
                message=f"Upserted pokemon moves for '{name}' into database",
            )

    except Exception as e:
        pretty_log(
            tag="db",
            message=f"Error upserting pokemon moves for '{name}': {e}",
        )

async def get_all_pokemon_moves(bot: discord.Client) -> list[tuple[str, list[str]]]:
    try:
        async with bot.pg_pool.acquire() as conn:
            rows = await conn.fetch("SELECT name, learned_by FROM pokemon_moves;")
            return [(row["name"], row["learned_by"]) for row in rows]
    except Exception as e:
        pretty_log(
            tag="db",
            message=f"Error fetching all pokemon moves: {e}",
        )
        return []

async def get_pokemon_learned_by(bot: discord.Client, name: str) -> list[str] | None:
    try:
        async with bot.pg_pool.acquire() as conn:
            row = await conn.fetchrow(
                "SELECT learned_by FROM pokemon_moves WHERE name = $1;", name
            )
            return row["learned_by"] if row else None
    except Exception as e:
        pretty_log(
            tag="db",
            message=f"Error fetching pokemon moves for '{name}': {e}",
        )
        return None
