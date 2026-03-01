import asyncio

import discord
from discord.ext import commands
from constants.ask_hattena.overall import STOPWORDS, TOPICS
from constants.straymons_constants import POKEMEOW_APPLICATION_ID
from utils.listener_func.perks_listener import perks_listener
from utils.listener_func.straydex_handler import straydex_command_handler
from utils.logs.pretty_log import pretty_log
from utils.listener_func.dex_listener import dex_listener
from utils.functions.ask_hattena import match_topic
PERK_BANNED_PHRASES = {"PokeMeow Clans — Perks Info", "PokeMeow Clans — Rank Info"}


def embed_has_field_name(embed, name_to_match: str) -> bool:
    """
    Returns True if any field name in the embed matches the given string.
    Returns False immediately if the embed has no fields.
    """
    if not hasattr(embed, "fields") or not embed.fields:
        return False
    for field in embed.fields:
        if field.name == name_to_match:
            return True
    return False


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
        # 🩷 Ask Hattena Topic Matching
        # ————————————————————————————————
        # if someone mentions Hattena or asks a question, try to match a topic and respond with the relevant embed
        HATTENA_MENTION = f"<@{self.bot.user.id}>"
        if HATTENA_MENTION in content:
            topic = match_topic(content)
            if topic:
                pretty_log(
                    "info",
                    f"User message matched topic '{topic}'. Triggering Straydex handler with topic command.",
                )
                topic_cmd = TOPICS[topic]["cmd"]
                topic_cmd = f"{PREFIX}{topic_cmd}"
                try:
                    await straydex_command_handler(
                        bot=self.bot,
                        message=message,
                        cmd=topic_cmd,
                    )
                except Exception as e:
                    pretty_log(
                        "error",
                        f"Error handling Straydex command for topic '{topic}': {e}",
                        include_trace=True,
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
        # ————————————————————————————————
        # 🩷 Dex Listener
        # ————————————————————————————————
        if first_embed:
            if embed_has_field_name(first_embed, "Dex Number"):
                pretty_log(
                    "info",
                    f"Detected dex command embed with 'Dex Number' field. Triggering dex listener.",
                )
                await dex_listener(self.bot, message)

# 🌈────────────────────────────────────────────
#        🛠️ Setup function to add cog to bot
# 🌈────────────────────────────────────────────
async def setup(bot: commands.Bot):
    await bot.add_cog(MessageCreateListener(bot))
