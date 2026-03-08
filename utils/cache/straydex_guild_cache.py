import discord

from utils.cache.cache_list import straydex_guild_cache
from utils.db.straydex_guild import get_all_straydex_guilds
from utils.logs.pretty_log import pretty_log


async def load_straydex_guild_cache(bot):
    """
    Load Straydex guild data from the database into the cache.
    """
    try:
        guilds = await get_all_straydex_guilds(bot)
        straydex_guild_cache.clear()
        for guild in guilds:
            straydex_guild_cache[guild["guild_id"]] = {
                "guild_name": guild["guild_name"],
                "update_channel_id": guild["update_channel_id"],
                "update_channel_name": guild["update_channel_name"],
            }
        pretty_log(
            "cache",
            f"Loaded Straydex guild cache with {len(straydex_guild_cache)} entries.",
        )
    except Exception as e:
        pretty_log(
            "error",
            f"Failed to load Straydex guild cache: {e}",
        )

def upsert_straydex_guild_cache(guild_id: int, guild_name: str, update_channel_id: int, update_channel_name: str):
    """
    Upsert a Straydex guild record in the cache.
    """
    straydex_guild_cache[guild_id] = {
        "guild_name": guild_name,
        "update_channel_id": update_channel_id,
        "update_channel_name": update_channel_name,
    }
    pretty_log(
        "cache",
        f"Upserted Straydex guild in cache: {guild_name} (ID: {guild_id}) with update channel {update_channel_name} (ID: {update_channel_id}).",
    )

def remove_straydex_guild_cache(guild_id: int):
    """
    Remove a Straydex guild record from the cache.
    """
    if guild_id in straydex_guild_cache:
        removed_guild = straydex_guild_cache.pop(guild_id)
        pretty_log(
            "cache",
            f"Removed Straydex guild from cache: {removed_guild['guild_name']} (ID: {guild_id}).",
        )
    else:
        pretty_log(
            "cache",
            f"Attempted to remove Straydex guild with ID: {guild_id} from cache, but it was not found.",
        )
        
def fetch_all_straydex_guild_w_update_channel_cache():
    """
    Fetch all Straydex guilds with their update channel information from the cache.
    """
    return {
        guild_id: {
            "guild_name": data["guild_name"],
            "update_channel_id": data["update_channel_id"],
            "update_channel_name": data["update_channel_name"],
        }
        for guild_id, data in straydex_guild_cache.items()
    }