import asyncio

import discord
from discord.ext import commands

from constants.straymons_constants import POKEMEOW_APPLICATION_ID
from utils.listener_func.perks_listener import perks_listener
from utils.listener_func.straydex_handler import straydex_command_handler
from utils.logs.pretty_log import pretty_log

PERK_BANNED_PHRASES = {"PokeMeow Clans — Perks Info", "PokeMeow Clans — Rank Info"}


# 🐾────────────────────────────────────────────
#        🌸 Message Create Listener Cog
# 🐾────────────────────────────────────────────
class MessageCreateListener(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 🦋 Helper: Retry Discord calls on 503
    async def retry_discord_call(self, func, *args, retries=3, delay=2, **kwargs):
        for attempt in range(1, retries + 1):
            try:
                return await func(*args, **kwargs)
            except discord.HTTPException as e:
                if e.status == 503 and attempt < retries:
                    await asyncio.sleep(delay)
                    continue
                raise

    # 🦋────────────────────────────────────────────
    #           👂 Message Listener Event
    # 🦋────────────────────────────────────────────
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        guild = message.guild
        if not guild:
            return  # Skip DMs
        if message.author.bot and message.author.id != POKEMEOW_APPLICATION_ID:
            return  # Ignore other bots except PokéMeow

        # ————————————————————————————————
        # 🩷 Variables
        # ————————————————————————————————
        content = message.content
        first_embed = message.embeds[0] if message.embeds else None
        embed_title = first_embed.title if first_embed else ""
        embed_description = first_embed.description if first_embed else ""
        embed_author_text = (
            first_embed.author.name if first_embed and first_embed.author else ""
        )
        embed_footer_text = (
            first_embed.footer.text if first_embed and first_embed.footer else ""
        )

        # ————————————————————————————————
        # 🩷 Straydex Handler
        # ————————————————————————————————
        PREFIX = "!"
        if message.content.startswith(PREFIX):
            try:
                await straydex_command_handler(
                    bot=self.bot,
                    message=message,
                )
            except Exception as e:
                pretty_log(
                    "error", f"Error handling Straydex command: {e}", include_trace=True
                )
        # ————————————————————————————————
        # 🩷 Perks Listener
        # ————————————————————————————————
        if "perks" in embed_author_text.lower() and not any(
            phrase in embed_author_text for phrase in PERK_BANNED_PHRASES
        ):
            try:
                await perks_listener(
                    bot=self.bot,
                    message=message,
                )
            except Exception as e:
                pretty_log(
                    "error", f"Error handling perks listener: {e}", include_trace=True
                )


# 🌈────────────────────────────────────────────
#        🛠️ Setup function to add cog to bot
# 🌈────────────────────────────────────────────
async def setup(bot: commands.Bot):
    await bot.add_cog(MessageCreateListener(bot))
