# 🍬 db/promo_team_utils.py - PostgreSQL Edition
import time

import asyncpg
import discord


async def check_if_there_is_promo_row(bot: discord.Client):
    query = "SELECT EXISTS (SELECT 1 FROM promo_team WHERE id = 1)"
    async with bot.pg_pool.acquire() as conn:
        row = await conn.fetchrow(query)
        return row["exists"] if row else False


# 🐣 1. Add new promo team (everything except ends_on)
async def add_promo_team(
    bot: discord.Client,
    message_id: int,
    promo_pokemon: str,
    promo_egg: str,
    mon1: str,
    item1: str,
    mon2: str,
    item2: str,
    mon3: str,
    item3: str,
    promo_egg_image: str = None,
    promo_pokemon_image: str = None,
):
    query = """
        INSERT INTO promo_team (
            id, message_id, promo_pokemon, promo_egg,
            mon1, item1, mon2, item2, mon3, item3,
            ends_on, promo_egg_image, promo_pokemon_image
        ) VALUES (1, $1, $2, $3, $4, $5, $6, $7, $8, $9, 0, $10, $11)
        ON CONFLICT (id) DO UPDATE SET
            message_id = EXCLUDED.message_id,
            promo_pokemon = EXCLUDED.promo_pokemon,
            promo_egg = EXCLUDED.promo_egg,
            mon1 = EXCLUDED.mon1,
            item1 = EXCLUDED.item1,
            mon2 = EXCLUDED.mon2,
            item2 = EXCLUDED.item2,
            mon3 = EXCLUDED.mon3,
            item3 = EXCLUDED.item3,
            ends_on = EXCLUDED.ends_on,
            promo_egg_image = EXCLUDED.promo_egg_image,
            promo_pokemon_image = EXCLUDED.promo_pokemon_image
    """
    async with bot.pg_pool.acquire() as conn:
        await conn.execute(
            query,
            message_id,
            promo_pokemon,
            promo_egg,
            mon1,
            item1,
            mon2,
            item2,
            mon3,
            item3,
            promo_egg_image,
            promo_pokemon_image,
        )


# 🍬 2. Edit all fields including ends_on
async def update_full_promo_team(
    bot: discord.Client,
    message_id: int,
    promo_pokemon: str,
    promo_egg: str,
    mon1: str,
    item1: str,
    mon2: str,
    item2: str,
    mon3: str,
    item3: str,
    ends_on: int,
    promo_egg_image: str = None,
    promo_pokemon_image: str = None,
):
    query = """
        UPDATE promo_team SET
            message_id = $1,
            promo_pokemon = $2, promo_egg = $3,
            mon1 = $4, item1 = $5,
            mon2 = $6, item2 = $7,
            mon3 = $8, item3 = $9,
            ends_on = $10,
            promo_egg_image = $11,
            promo_pokemon_image = $12
        WHERE id = 1
    """
    async with bot.pg_pool.acquire() as conn:
        await conn.execute(
            query,
            message_id,
            promo_pokemon,
            promo_egg,
            mon1,
            item1,
            mon2,
            item2,
            mon3,
            item3,
            ends_on,
            promo_egg_image,
            promo_pokemon_image,
        )


# 🍬 3. Update ends_on only
# Update ends_on where id = 1; if there is no row, upsert new row with empty values except ends_on and id = 1
async def update_ends_on(bot: discord.Client, ends_on: int):
    query = """
        INSERT INTO promo_team (
            id, ends_on
        ) VALUES (1, $1)
        ON CONFLICT (id) DO UPDATE SET
            ends_on = EXCLUDED.ends_on
    """
    async with bot.pg_pool.acquire() as conn:
        await conn.execute(query, ends_on)


# 🍬 4. Delete the only row
async def delete_promo_team(bot: discord.Client):
    query = "DELETE FROM promo_team"
    async with bot.pg_pool.acquire() as conn:
        await conn.execute(query)


# 🍬 5. Get everything except ends_on
async def get_promo_team_data(bot: discord.Client):
    query = """
        SELECT message_id, promo_pokemon, promo_egg,
               mon1, item1, mon2, item2, mon3, item3,
               promo_egg_image, promo_pokemon_image
        FROM promo_team WHERE id = 1
    """
    async with bot.pg_pool.acquire() as conn:
        return await conn.fetchrow(query)


# 🍬 6. Get only ends_on
async def get_ends_on(bot: discord.Client):
    query = "SELECT ends_on FROM promo_team WHERE id = 1"
    async with bot.pg_pool.acquire() as conn:
        row = await conn.fetchrow(query)
        return row["ends_on"] if row else None


# 🍬 7. Update promo team without modifying ends_on
async def update_promo_team_only(
    bot: discord.Client,
    message_id: int,
    promo_pokemon: str,
    promo_egg: str,
    mon1: str,
    item1: str,
    mon2: str,
    item2: str,
    mon3: str,
    item3: str,
    promo_egg_image: str = None,
    promo_pokemon_image: str = None,
):
    query = """
        UPDATE promo_team SET
            promo_pokemon = $1,
            promo_egg = $2,
            mon1 = $3,
            item1 = $4,
            mon2 = $5,
            item2 = $6,
            mon3 = $7,
            item3 = $8,
            promo_egg_image = $9,
            promo_pokemon_image = $10
        WHERE id = 1
    """
    async with bot.pg_pool.acquire() as conn:
        await conn.execute(
            query,
            promo_pokemon,
            promo_egg,
            mon1,
            item1,
            mon2,
            item2,
            mon3,
            item3,
            promo_egg_image,
            promo_pokemon_image,
        )


# 🍬 8. Get just the message_id of current promo team
async def get_promo_team_message_id(bot: discord.Client):
    query = "SELECT message_id FROM promo_team WHERE id = 1"
    async with bot.pg_pool.acquire() as conn:
        row = await conn.fetchrow(query)
        return row["message_id"] if row else None


# 🍬 9. Get all expired promos (message_id, promo_pokemon, ends_on)
async def get_expired_promos(bot: discord.Client, current_unix: int):
    query = """
        SELECT message_id, promo_pokemon, ends_on
        FROM promo_team
        WHERE ends_on <= $1 AND id = 1
    """
    async with bot.pg_pool.acquire() as conn:
        rows = await conn.fetch(query, current_unix)
        return rows


async def is_promo_over(bot: discord.Client):
    """Check if the current promo is over by comparing ends_on with current time."""
    current_unix = int(time.time())
    query = "SELECT ends_on FROM promo_team WHERE id = 1"
    async with bot.pg_pool.acquire() as conn:
        row = await conn.fetchrow(query)
        if not row:
            return False  # No promo team data means no active promo
        ends_on = row["ends_on"]
        if ends_on is None or ends_on == 0:
            return False  # If ends_on is not set or 0, promo is not over
        return ends_on <= current_unix
