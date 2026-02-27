import asyncio

import discord
from discord.ext import commands

from constants.straymons_constants import POKEMEOW_APPLICATION_ID
from utils.listener_func.dex_listener import dex_listener

from utils.logs.pretty_log import pretty_log

from .on_message_create import embed_has_field_name


class MessageEditListener(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):

        # Only process in straymons server and avoid dms
        if after.guild is None:
            return

        # 🚫 Ignore bots except PokéMeow
        if (
            after.author.bot
            and after.author.id != POKEMEOW_APPLICATION_ID
            and not after.webhook_id
        ):
            return

        # ✨───────────────────────────────────────────────✨
        # 🪻 Message Variables
        # ✨───────────────────────────────────────────────✨
        embed = after.embeds[0] if after.embeds else None
        embed_desc = embed.description if embed else ""
        embed_color = embed.color.value if embed else None

        content = after.content if after.content else ""
        first_embed = after.embeds[0] if after.embeds else None
        first_embed_author_text = (
            first_embed.author.name if first_embed and first_embed.author else ""
        )
        first_embed_description = first_embed.description if first_embed else ""
        first_embed_footer_text = (
            first_embed.footer.text if first_embed and first_embed.footer else ""
        )
        first_embed_title = first_embed.title if first_embed else ""

        # ✨───────────────────────────────────────────────✨
        # 🪻 DEX LISTENER
        # ✨───────────────────────────────────────────────✨
        if first_embed:
            if embed_has_field_name(first_embed, "Dex Number"):
                pretty_log(
                    "info",
                    f"Detected dex command embed with 'Dex Number' field. Triggering dex listener.",
                )
                await dex_listener(self.bot, after)


async def setup(bot: commands.Bot):
    await bot.add_cog(MessageEditListener(bot))
