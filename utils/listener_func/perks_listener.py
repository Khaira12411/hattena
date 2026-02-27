import re

import discord

from utils.cache.cache_list import straymon_member_cache
from utils.db.straymon_db import update_catch_rate, update_patreon_status
from utils.functions.get_pokemeow_reply import get_pokemeow_command_user
from utils.logs.pretty_log import pretty_log


async def perks_listener(
    bot: discord.Client,
    message: discord.Message,
):

    member = await get_pokemeow_command_user(message)
    if not member:
        return

    user_id = member.id
    # Check if the user is in the Straymon member cache
    if user_id not in straymon_member_cache:
        return

    embed = message.embeds[0]
    if not embed:
        return

    description = embed.description or ""

    # 🛑 Extract catch boost
    catchboost_match = re.search(r"Catch boost\*\*: \+?([\d.]+)%", description)
    catchboost = float(catchboost_match.group(1)) if catchboost_match else 0.0

    # 🛑 Check if "ninja" is in description → is_patreon
    is_patreon = "ninja" in description.lower()

    # Get old values from cache for logging
    old_data = straymon_member_cache.get(user_id, {})
    old_catch_rate = old_data.get("catch_rate_bonus", 0)
    old_patreon_status = old_data.get("is_patreon", False)

    if catchboost != old_catch_rate:
        await update_catch_rate(bot, user_id, int(catchboost))
        pretty_log(
            "info",
            f"Updated catch rate for user_id {user_id} from {old_catch_rate}% to {catchboost}%",
            label="💠 STRAYMON PERKS LISTENER",
            bot=bot,
        )
    if is_patreon != old_patreon_status:
        await update_patreon_status(bot, user_id, is_patreon)
        pretty_log(
            "info",
            f"Updated Patreon status for user_id {user_id} from {old_patreon_status} to {is_patreon}",
            label="💠 STRAYMON PERKS LISTENER",
            bot=bot,
        )
