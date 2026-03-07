# ❀───────────────────────────────❀
#       💖  Imports  💖
# ❀───────────────────────────────❀
import asyncio
import glob
import logging
import os
import random
from datetime import datetime
from zoneinfo import ZoneInfo

import discord
from discord import app_commands
from discord.ext import commands, tasks
from dotenv import load_dotenv

from utils.cache.cache_list import clear_processed_ids_cache
from utils.cache.central_cache_loader import load_all_caches
from utils.db.get_pg_pool import *
from utils.logs.pretty_log import pretty_log, set_hatenna_bot

# ❀───────────────────────────────❀
#       💖  Suppress Logs  💖
# ❀───────────────────────────────❀
"""logging.basicConfig(level=logging.CRITICAL)
for logger_name in [
    "discord",
    "discord.gateway",
    "discord.http",
    "discord.voice_client",
    "asyncio",
]:
    logging.getLogger(logger_name).setLevel(logging.CRITICAL)
logging.getLogger("discord.client").setLevel(logging.CRITICAL)
"""
# ❀───────────────────────────────❀
#       💖  Bot Factory  💖
# ❀───────────────────────────────❀
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
set_hatenna_bot(bot)


# ❀───────────────────────────────❀
#       💖  Task Refresh Every 1 Hour 💖
# ❀───────────────────────────────❀
@tasks.loop(minutes=60)
async def refresh_all_caches():

    # Removed first-run skip logic so cache loads immediately
    await load_all_caches(bot)

    # Clear processed IDs cache every hour to prevent unbounded growth
    clear_processed_ids_cache()


# ❀───────────────────────────────❀
#   💖  Prefix Command Error Handler 💖
# ❀───────────────────────────────❀
@bot.event
async def on_command_error(ctx, error):
    # Ignore prefix command not found
    if isinstance(error, commands.CommandNotFound):
        return

    # Handle other prefix errors
    await ctx.send("❌ Something went wrong.")
    pretty_log(
        tag="error",
        message=f"Prefix command error: {error}",
        include_trace=True,
    )


# ❀───────────────────────────────❀
#      💖  Startup Checklist 💖
# ❀───────────────────────────────❀
async def startup_checklist(bot: commands.Bot):
    from utils.cache.cache_list import (
        market_value_cache,
        straymon_member_cache,
        webhook_url_cache,
    )

    total_market_values = len(market_value_cache)
    # ❀ This divider stays untouched ❀
    print("\n୨୧ ⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔♡⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔ ୨୧")
    print(f"✅ {len(bot.cogs)} 🌷 Cogs Loaded")
    print(f"✅ {len(straymon_member_cache)} 🌸 Straymon Members")
    print(f"✅ {total_market_values:,} 💎 Market Values")
    print(f"✅ {len(webhook_url_cache)} 🍧 Webhook Urls")
    pg_status = "Ready" if hasattr(bot, "pg_pool") else "Not Ready"
    print(f"✅ {pg_status} 🧁  PostgreSQL Pool")
    total_slash_commands = sum(1 for _ in bot.tree.walk_commands())
    print(f"✅ {total_slash_commands} 🧸 Slash Commands Synced")
    print("୨୧ ⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔♡⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔⏔ ୨୧\n")


# ❀───────────────────────────────❀
#       💖  Event Hooks 💖
# ❀───────────────────────────────❀
# ❀ On Ready ❀
@bot.event
async def on_ready():
    pretty_log("ready", f"Hattena bot awake as {bot.user}")

    # ❀ Sync slash commands ❀
    await bot.tree.sync()

    # ❀ Log how many slash commands were synced ❀
    total_commands = len(bot.tree.get_commands())
    pretty_log("ready", f"Synced {total_commands} slash commands.")

    # Load all caches immediately on startup
    await load_all_caches(bot)

    # Start the cache refresh task if it's not already running
    if not refresh_all_caches.is_running():
        refresh_all_caches.start()
        pretty_log(message="✅ Started cache refresh task", tag="ready")

    # ❀ Run startup checklist ❀
    await startup_checklist(bot)

    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=" 💜 !h")
    )


# ❀───────────────────────────────❀
#       💖  Setup Hook 💖
# ❀───────────────────────────────❀
@bot.event
async def setup_hook():
    # ❀ PostgreSQL connection ❀
    try:
        bot.pg_pool = await get_pg_pool()
    except Exception as e:
        pretty_log("critical", f"Postgres connection failed: {e}", include_trace=True)

    # ❀ Load all cogs, skip __init__.py ❀
    for cog_path in glob.glob("cogs/**/*.py", recursive=True):
        if os.path.basename(cog_path) == "__init__.py":
            continue
        relative_path = os.path.relpath(cog_path, "cogs")
        module_name = relative_path[:-3].replace(os.sep, ".")
        cog_name = f"cogs.{module_name}"
        try:
            await bot.load_extension(cog_name)
        except Exception as e:
            pretty_log("error", f"Failed to load {cog_name}: {e}", include_trace=True)


# ❀───────────────────────────────❀
#       💖  Main Async Runner 💖
# ❀───────────────────────────────❀
async def main():
    load_dotenv()
    pretty_log("ready", "Hattena Bot is starting...")

    retry_delay = 5
    while True:
        try:
            await bot.start(os.getenv("DISCORD_TOKEN"))
        except KeyboardInterrupt:
            pretty_log("ready", "Shutting down Hattena Bot...")
            break
        except Exception as e:
            pretty_log("error", f"Bot crashed: {e}", include_trace=True)
            pretty_log("ready", f"Restarting Hattena Bot in {retry_delay} seconds...")
            await asyncio.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 60)


# ❀───────────────────────────────❀
#       💖  Entry Point 💖
# ❀───────────────────────────────❀
if __name__ == "__main__":
    asyncio.run(main())
