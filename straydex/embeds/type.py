import discord

from straydex.desc import SD_TYPE_DESC
from straydex.functions.main import (
    get_default_footer,

)
from utils.logs.pretty_log import pretty_log
from utils.visuals.type_embed import TYPE_EMOJIS

async def build_sd_type_embed(
    guild: discord.Guild,
    main_cmd: str,
    color: str,
    user_display_name: str,
    image_url: str = None,
    thumbnail_url: str = None,
):

    try:
        type_name = main_cmd.upper() 
        emoji = TYPE_EMOJIS.get(main_cmd.lower(), "")
        display_type = f"{emoji} {type_name}" if emoji else type_name
        display_type_str = f"# {display_type} TYPE\n"
        desc = display_type_str + SD_TYPE_DESC
        embed = discord.Embed(description=desc, color=color)
        if thumbnail_url:
            embed.set_thumbnail(url=thumbnail_url)  # fix here
        if image_url:
            embed.set_image(url=image_url)
        footer_text = get_default_footer(user_display_name)
        embed.set_footer(
            text=footer_text, icon_url=guild.icon.url if guild.icon else None
        )
        embed.set_author(name="STRAYDEX")

        return embed
    except Exception as e:
        pretty_log(
            tag="error",
            label="SD Type Embed",
            message=f"❌ Error building SD Type embed: {e}",
        )
        return None
