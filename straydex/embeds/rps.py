
import discord
from discord.ui import Button, View

from constants.aesthetic import Dividers, Emojis
from straydex.config import SD_CONFIG
from straydex.desc import RPS_DESC, SD_MAIN_IMAGES
from straydex.functions.main import get_default_footer
from utils.logs.pretty_log import pretty_log


# ❀───────────────────────────────❀
#       💖  RPS Embeds  💖
# ❀───────────────────────────────❀
async def build_sd_rps_main_info_embed(
    guild: discord.Guild,
    user_display_name: str,
    user_id: int,
):
    desc = RPS_DESC.info
    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)
    footer_text = get_default_footer(user_display_name)
    icon_url = guild.icon.url if guild.icon else None
    embed.set_footer(text=footer_text, icon_url=icon_url)
    embed.set_image(url=SD_MAIN_IMAGES.RPS)
    embed.set_author(name="STRAYDEX")
    return embed, None, None 