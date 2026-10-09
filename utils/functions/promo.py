import discord
from discord.ext import commands
from utils.db.promo_team_db import *
from utils.logs.pretty_log import pretty_log
from utils.functions.pokemon_func import get_display_name
from utils.functions.text import clean_multiline_string
from utils.functions.colors import get_random_pastel_blue
TESTING = True
# 🌼─────────────────────────────────────────
#       📖 Embed: /promo-team Command View
# 🌼─────────────────────────────────────────
def build_promo_team_command_embed(
    promo_pokemon: str,
    promo_egg: str,
    mon1: str,
    item1: str,
    mon2: str,
    item2: str,
    mon3: str,
    item3: str,
    ends_on: int = None,
    promo_egg_image: str = None,
    promo_pokemon_image: str = None,
    guild_icon_url: str = None,
):
    promo_pokemon_display = get_display_name(promo_pokemon)
    promo_egg_display = get_display_name(promo_egg)
    desc = clean_multiline_string(
        f"""
# PROMO INFO
POKEMON: {promo_pokemon_display}
EGG: {promo_egg_display}
COMMAND: `/promo-team` or `!promo`
> - ;t add {mon1} 1
> - ;t give {item1} {mon1}
> - ;t add {mon2} 2
> - ;t give {item2} {mon2}
> - ;t add {mon3} 3
> - ;t give {item3} {mon3}
> - ;t defend
> - ;u
"""
    )

    if ends_on is not None:
        desc += f"\n🗓️ Promo ends on <t:{ends_on}:f>"
    footer_text = "To get more info about the items, visit our Straydex `!h"
    embed = discord.Embed(description=desc, color=get_random_pastel_blue())
    if promo_pokemon_image:
        embed.set_image(url=promo_pokemon_image)
    if promo_egg_image:
        embed.set_thumbnail(url=promo_egg_image)

    embed.set_footer(
        text=footer_text, icon_url=guild_icon_url if guild_icon_url else None
    )

    return embed

async def get_promo_team_embed_and_msg_id(bot: commands.Bot) -> discord.Embed:
    from utils.db.promo_team_db import get_ends_on, get_promo_team_data

    data = await get_promo_team_data(bot=bot)
    if not data:
        return None, None
    ends_on = await get_ends_on(bot=bot)
    (
        message_id,
        promo_pokemon,
        promo_egg,
        mon1,
        item1,
        mon2,
        item2,
        mon3,
        item3,
        promo_egg_image,
        promo_pokemon_image,
    ) = data

    embed = build_promo_team_command_embed(
        promo_pokemon=promo_pokemon,
        promo_egg=promo_egg,
        mon1=mon1,
        item1=item1,
        mon2=mon2,
        item2=item2,
        mon3=mon3,
        item3=item3,
        promo_egg_image=promo_egg_image,
        promo_pokemon_image=promo_pokemon_image,
        ends_on=ends_on,
    )

    return embed, message_id


async def promo_autoresponder(bot: discord.Client, message: discord.Message):
    """🍃 Sends the current available promo team"""
    embed, _ = await get_promo_team_embed_and_msg_id(bot=bot)
    if not embed:
        return  # No promo team available, so we don't send anything
    await message.reply(embed=embed, mention_author=False)
