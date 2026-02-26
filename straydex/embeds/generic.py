import discord
from discord.ui import Button, View

from constants.aesthetic import Dividers
from constants.perks import perks
from constants.straymons_constants import STRAYMONS_GUILD_ID
from utils.logs.pretty_log import pretty_log

# If you need main_cmd_list, import it inside the function that uses it:
# def some_function(...):
#     from straydex.AR.h import main_cmd_list
#     ...
from straydex.config import SD_CONFIG
from straydex.functions.main import (
    get_default_footer,
    remove_line_from_desc,
    send_sd_logs,
)

main_cmd_list = [
    "h",
    "ac",
    "ba",
    "co",
    "ev",
    "ex",
    "fa",
    "it",
    "mc",
    "po",
    "!tr",
    "!ty",
    "wb",
    "bg",
    "straymon",
    "mr",
    "ic",
]
battle_sub_cmd_list = ["bati", "bareg", "baic"]
ubg_sub_cmd_list = [
    "ubgcas",
    "ubgcat",
    "ubgcos",
    "ubgcur",
    "ubgdai",
    "ubgfid",
    "ubgfis",
    "ubgloc",
    "ubglvl",
    "ubgpok",
    "ubgres",
    "ubgswa",
    "ubgtra",
]

STRAYMONS_ONLY_COMMANDS = [
    "straymon",
    "ubg",
]
async def build_sd_main_embed(
    guild: discord.Guild,
    main_cmd: str,
    text: str,
    user_display_name: str,
    image_url: str = None,
    cmd: str = None,
):


    if main_cmd == "h":
        # Remove this line from the description if not in Straymons guild
        line = "- **`!STRAYMON`**  Straymon Clan"
        text = remove_line_from_desc(guild.id, line, text)
        line = "- **`!UBG`**  Ultimate Beginner Guide"
        text = remove_line_from_desc(guild.id, line, text)

    # Determine header text
    if cmd in battle_sub_cmd_list:
        header_text = "STRAYDEX: BATTLE"
    elif cmd in ubg_sub_cmd_list:
        header_text = "ULTIMATE BEGINNER GUIDE"
    else:
        header_text = "STRAYDEX"

    # Set up embed
    embed = discord.Embed(description=text, color=SD_CONFIG.default_color)
    embed.set_image(url=image_url if image_url else Dividers.SD_Alternate)
    embed.set_footer(
        text=get_default_footer(user_display_name), icon_url=guild.icon.url
    )

    # Thumbnail or author logic
    if cmd in main_cmd_list and main_cmd == "h":
        embed.set_thumbnail(url=SD_CONFIG.default_thumbnail)
    else:
        embed.set_author(name=header_text)

    return embed


async def build_sd_two_embed(
    guild: discord.Guild,
    main_cmd: str,
    text: str,
    user_display_name: str,
    image_url: str = None,
    image_url_second: str = None,
    text_second: str = None,
):
    #pretty_log("debug", f"Building embed for command: {main_cmd}")
    if main_cmd in STRAYMONS_ONLY_COMMANDS and guild.id != STRAYMONS_GUILD_ID:
        return None  # Don't build embed for Straymons-only commands in other guilds

    if main_cmd == "ubg":
        author_text = "ULTIMATE BEGINNER GUIDE"
    else:
        author_text = "STRAYDEX"

    first_embed = discord.Embed(description=text, color=SD_CONFIG.default_color)
    first_embed.set_image(url=image_url)
    first_embed.set_author(name=author_text)
    footer_text = get_default_footer(user_display_name)
    second_embed = discord.Embed(description=text_second, color=SD_CONFIG.default_color)
    second_embed.set_footer(text=footer_text, icon_url=guild.icon.url)
    second_embed.set_image(url=image_url_second)
    if main_cmd == "straymon":
        thumbnail = perks["diamond"]["thumbnail_url"]
        first_embed.set_thumbnail(url=thumbnail)
        second_embed.set_thumbnail(url=thumbnail)

    return [first_embed, second_embed]
