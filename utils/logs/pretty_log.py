# 🌸───────────────────────────────────────────────🌸
#                Pretty Logger (Pink)
# 🌸───────────────────────────────────────────────🌸
import traceback
from datetime import datetime

import discord
from discord.ext import commands

BOT_INSTANCE: commands.Bot | None = None


def set_hattena_bot(bot: commands.Bot):
    global BOT_INSTANCE
    BOT_INSTANCE = bot


# 🎀 Pink aesthetic tags (warn/critical keep non-pink)
PINK_TAGS = {
    "info": "🌸 Info",
    "db": "🍡 Database",
    "cmd": "💖 Cmd",
    "ready": "🌷 Ready",
    "success": "🧁 Success",
    "error": "❌ Error",  # red for clarity
    "warn": "⚠️ Warn",  # yellow for clarity
    "critical": "🚨 Critical",  # red for clarity
    "skip": "🩷 Skip",
    "sent": "📮 Sent",
    "missing": "🐰 Missing Pokemon",
    "debug": "🍑 Debug",
    "cache": "🍥 Cache",
    "sync": "🌼 Sync",
    "market_alert": "🦄 Market Alert",
    "background_task": "🌙 Background Task",
    "quest": "🎀 Quest",
    "ui": "👚 View",
    "auction": "🍭 Auction",
}

# 🎨 ANSI color palette (soft pinks + red/yellow highlights)
COLOR_HATENNA_BLUE = "\033[38;2;163;199;247m"  # Hatenna Light Blue
COLOR_HATENNA_PURPLE = "\033[38;2;109;92;164m"  # Hatenna Soft Purple
COLOR_WARN = "\033[38;2;237;201;100m"  # soft golden yellow (unchanged)
COLOR_ERROR = "\033[38;2;220;80;120m"  # soft red (unchanged)
COLOR_RESET = "\033[0m"

# Critical logs to Discord channel
CRITICAL_LOG_CHANNEL_ID = 1444997181244444672  # CC Error Logs


# 🌸───────────────────────────────────────────────🌸
#                Pretty Logger Function
# 🌸───────────────────────────────────────────────🌸
def pretty_log(
    tag: str,
    message: str,
    *,
    label: str = None,
    bot: commands.Bot = None,
    include_trace: bool = True,
):
    """Pretty pink logger with Discord integration."""

    # 🌸 Build prefix only if tag is not empty
    prefix = PINK_TAGS.get(tag, tag) if tag else None
    prefix_part = f"[{prefix}] " if prefix else ""

    label_str = f"[{label}] " if label else ""

    # 🌸 choose color
    if tag in ("critical", "error"):
        color = COLOR_ERROR
    elif tag == "warn":
        color = COLOR_WARN
    elif tag == "ui":
        color = COLOR_HATENNA_PURPLE
    else:
        color = COLOR_HATENNA_BLUE
    now = datetime.now().strftime("%H:%M:%S")

    # print to console
    log_message = f"{color}[{now}] {prefix_part}{label_str}{message}{COLOR_RESET}"
    print(log_message)

    # show traceback
    if include_trace and tag in ("error", "critical"):
        traceback.print_exc()

    # send to Discord channel if critical
    bot_to_use = bot or BOT_INSTANCE
    if bot_to_use and tag in ("critical", "error", "warn"):
        try:
            channel = bot_to_use.get_channel(CRITICAL_LOG_CHANNEL_ID)
            if channel:
                full_message = f"{prefix_part}{label_str}{message}"
                if include_trace and tag in ("error", "critical"):
                    full_message += f"\n```py\n{traceback.format_exc()}```"
                if len(full_message) > 2000:
                    full_message = full_message[:1997] + "..."
                bot_to_use.loop.create_task(channel.send(full_message))
        except Exception:
            print(
                f"{COLOR_ERROR}[❌ Logger Error] Failed to send log to channel{COLOR_RESET}"
            )
            traceback.print_exc()
