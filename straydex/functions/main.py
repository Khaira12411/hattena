import discord

from constants.straymons_constants import STRAYMONS__TEXT_CHANNELS, STRAYMONS_GUILD_ID
from straydex.config import SD_CONFIG
from utils.cache.global_variables import TESTING
from utils.functions.webhook import send_webhook
from utils.logs.pretty_log import pretty_log


async def send_sd_logs(
    bot: discord.Client,
    main_cmd: str,
    user: discord.User,
    channel: discord.TextChannel,
    cmd: str = None,
):
    if TESTING:
        return  # Skip logging in testing mode
    commands_str = ""
    question_str = ""
    if cmd:
        question = main_cmd.replace(f"<@{bot.user.id}>", "").title().strip()
        question_str = f"- **Question:** `{question}`\n"
        commands_str = f"- **Command:** `{cmd}`\n"
    else:
        commands_str = f"- **Command:** `{main_cmd}`\n"

    # Build and return your embed here (example)
    text = (
        f"- **User:** {user.mention} (ID: {user.id})\n"
        f"{question_str}"
        f"{commands_str}"
        f"- **Guild:** {channel.guild.name} (ID: {channel.guild.id})\n"
        f"- **Channel:** {channel.mention} (ID: {channel.id})"
    )
    embed = discord.Embed(description=text, color=SD_CONFIG.default_color)
    embed.set_author(name=user.name, icon_url=user.avatar.url if user.avatar else None)
    straymon_guild = bot.get_guild(STRAYMONS_GUILD_ID)
    if not straymon_guild:
        pretty_log(
            tag="error",
            message=f"Failed to find Straymons guild with ID {STRAYMONS_GUILD_ID}",
        )
        return

    # Send to logs channel
    straydex_logs_channel = straymon_guild.get_channel(
        STRAYMONS__TEXT_CHANNELS.straydex_logs
    )
    if straydex_logs_channel:
        try:
            await send_webhook(
                channel=straydex_logs_channel,
                embed=embed,
                bot=bot,
            )
            pretty_log(
                tag="straydex",
                message=f"Sent Straydex log for command '{main_cmd}' by user '{user}' in channel '{channel.name}'",
            )
        except Exception as e:
            pretty_log(
                tag="error",
                message=f"Failed to send log to Straydex logs channel: {e}",
            )


def get_straydex_line(guild_id: int, line: str) -> bool:
    if guild_id == STRAYMONS_GUILD_ID:
        return line
    return ""


def is_straymons_guild(guild_id: int) -> bool:
    if guild_id == STRAYMONS_GUILD_ID:
        return True
    return False


def remove_line_from_desc(guild_id: int, line: str, desc: str):

    if not is_straymons_guild(guild_id):
        return desc.replace(line, "").strip()
    return desc


def get_default_footer(user_display_name: str):
    # Generate the footer string dynamically
    return f"StrayDex inquiry by {user_display_name}"
