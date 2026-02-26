import discord
from straydex.desc import SD_TYPE_DESC
from straydex.functions.main import (
    remove_line_from_desc,
    send_sd_logs,
    get_default_footer,
)
from utils.logs.pretty_log import pretty_log

async def build_sd_type_embed(
    guild: discord.Guild,
    main_cmd: str,
    color: str,
    user_display_name: str,
    image_url: str = None,
    thumbnail_url: str = None,
):
    try:
        embed = discord.Embed(description=SD_TYPE_DESC, color=color)
        if thumbnail_url:
            embed.set_thumbnail(url=thumbnail_url)  # fix here
        if image_url:
            embed.set_image(url=image_url)
        footer_text = get_default_footer(user_display_name)
        embed.set_footer(text=footer_text, icon_url=guild.icon.url)
        embed.set_author(name="STRAYDEX")

        return embed
    except Exception as e:
        pretty_log(
            tag="error",
            label="SD Type Embed",
            message=f"❌ Error building SD Type embed: {e}",
        )
        return None