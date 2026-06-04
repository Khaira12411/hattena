import discord

from constants.aesthetic import Dividers, Emojis
from straydex.config import SD_CONFIG
from straydex.desc import SD_VI_TIER_DESC
from straydex.functions.main import get_default_footer
from utils.logs.pretty_log import pretty_log

image_url = "https://play.pokemonshowdown.com/sprites/xyani/vivillon-elegant.gif"
# ❀───────────────────────────────❀
#       💖  VI Embed  💖
# ❀───────────────────────────────❀
async def build_sd_vi_main_info_embed(
    message: discord.Message,
):
    user_display_name = message.author.display_name
    guild = message.guild
    try:
        desc = "# VIVILLON FORMS SERVERS"
        embed = discord.Embed(description=desc, color=SD_CONFIG.default_color)
        footer_text = get_default_footer(user_display_name)
        icon_url = guild.icon.url if guild.icon else None
        embed.set_footer(text=footer_text, icon_url=icon_url)
        embed.set_thumbnail(url=image_url)
        embed.set_image(url=Dividers.SD_Alternate)
        embed.set_author(name="STRAYDEX")
        embed.add_field(name="Tier 1", value=SD_VI_TIER_DESC.one, inline=False)
        embed.add_field(name="Tier 2", value=SD_VI_TIER_DESC.two, inline=False)
        embed.add_field(name="Tier 3", value=SD_VI_TIER_DESC.three, inline=False)
        embed.add_field(name="Tier 4", value=SD_VI_TIER_DESC.four, inline=False)
        embed.add_field(name="Tier 5", value=SD_VI_TIER_DESC.five, inline=False)
        await message.reply(embed=embed)

    except Exception as e:
        pretty_log(
            tag="error",
            message=f"Error building VI main info embed: {e}",
            include_trace=True,
        )

