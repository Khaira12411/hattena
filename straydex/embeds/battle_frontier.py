import discord

from straydex.config import SD_CONFIG
from straydex.desc.battle_frontier import *
from straydex.functions.main import get_default_footer

abbrv_map = {
    "pal": "palace",
    "are": "arena",
    "tow": "tower",
}


async def build_sd_bf_main_info_embed(
    guild: discord.Guild, user_display_name: str, sub_cmd: str
):

    abbrv = abbrv_map.get(sub_cmd, sub_cmd)
    desc = getattr(BF_DESC, abbrv)
    author_image_url = getattr(BF_AUTHOR_IMAGE_URL, abbrv)
    thumbnail_url = getattr(BF_THUMBNAIL, abbrv)
    image_url = getattr(BF_IMAGE_URL, abbrv)
    embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)
    footer_text = get_default_footer(user_display_name)
    icon_url = guild.icon.url if guild.icon else None
    embed.set_footer(text=footer_text, icon_url=icon_url)
    embed.set_image(url=image_url)
    embed.set_thumbnail(url=thumbnail_url)
    embed.set_author(name="STRAYDEX", icon_url=author_image_url)
    content = f" # STRAYDEX BATTLE FRONTIER"
    return embed, content
