import asyncio

import discord
from discord.ext import commands

from constants.ask_hattena.overall import STOPWORDS, TOPICS
from constants.straymons_constants import MH_APP_ID, POKEMEOW_APPLICATION_ID
from utils.functions.ask_hattena import match_topic
from utils.listener_func.dex_listener import dex_listener
from utils.listener_func.market_view_listener import market_view_listener
from utils.listener_func.mh_lookup_listener import lookup_listener
from utils.listener_func.perks_listener import perks_listener
from utils.listener_func.straydex_handler import straydex_command_handler
from utils.logs.pretty_log import pretty_log

PERK_BANNED_PHRASES = {"PokeMeow Clans — Perks Info", "PokeMeow Clans — Rank Info"}
ignore_prefix_commands = [
    "!pray",
    "!daily",
    "!rps",
    "!dice",
    "!claw",
    "!roulette",
    "!guess",
    "!eat",
    "!items",
]


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

        # ————————————————————————————————
        # 🩵 MH Lookup Listener
        # ————————————————————————————————
        if message.author.bot and message.author.id == MH_APP_ID:
            if message.embeds and message.embeds[0]:
                if embed_has_field_name(message.embeds[0], "Lowest Market"):
                    pretty_log(
                        "info",
                        f"Detected MH lookup embed with 'Lowest Market' field. Triggering MH lookup listener.",
                    )
                    await lookup_listener(self.bot, message)
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
        first_embed_author = (
            first_embed.author.name if first_embed and first_embed.author else ""
        )
        # ————————————————————————————————
        # 🩷 Straydex Handler
        # ————————————————————————————————
        PREFIX = "!"
        cmd_word = message.content.split()[0] if message.content else ""
        if cmd_word.startswith(PREFIX) and cmd_word.lower() not in [
            c.lower() for c in ignore_prefix_commands
        ]:
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
            # Check for weakness question pattern
            import re

            weakness_patterns = [
                r"what is ([\w\-'. ]+) weak to",
                r"weakness(?:es)? of ([\w\-'. ]+)",
                r"([\w\-'. ]+) weakness(?:es)?",
                r"([\w\-'. ]+) type weakness",
                r"what type is ([\w\-'. ]+) weak to",
                r"weakness for ([\w\-'. ]+)",
                r"what is (?:super|2x|4x|0x|1x|1/2x|1/4x) effective against ([\w\-'. ]+)",
                r"which types are (?:super|2x|4x|0x|1x|1/2x|1/4x) effective against ([\w\-'. ]+)",
                r"what is (?:super|2x|4x|0x|1x|1/2x|1/4x) effective on ([\w\-'. ]+)",
                r"([\w\-'. ]+) (?:super|2x|4x|0x|1x|1/2x|1/4x) weakness",
                r"what is effective against ([\w\-'. ]+)",
                r"what are effective against ([\w\-'. ]+)",
            ]
            matched_pokemon = None
            for pattern in weakness_patterns:
                match = re.search(pattern, content, re.IGNORECASE)
                if match:
                    matched_pokemon = match.group(1).strip()
                    break
            if matched_pokemon:
                from utils.visuals.type_embed import build_weakness_embed_from_input

                try:
                    embed_result = build_weakness_embed_from_input(matched_pokemon)
                    if embed_result is None:
                        await message.reply(
                            f"Could not find weakness information for '{matched_pokemon}'."
                        )
                    else:
                        weakness_embed, _, _ = embed_result
                        await message.reply(embed=weakness_embed)
                    return
                except Exception as e:
                    pretty_log(
                        "error",
                        f"Error building weakness embed for '{matched_pokemon}': {e}",
                        include_trace=True,
                    )
                    await message.reply(
                        f"Sorry, I had trouble fetching weakness information for '{matched_pokemon}'."
                    )
                    return
            # Fallback to topic matching if not a weakness question
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
                await dex_listener(self.bot, message)

        # ————————————————————————————————
        # 🩷 MARKET VIEW LISTENER
        # ————————————————————————————————
        if (
            first_embed
            and "PokeMeow Global Market" in first_embed_author
            and not "Recent" in first_embed_author
            and not "Rarity" in first_embed_author
        ):
            pretty_log(
                tag="info",
                message=f"Processing market view message with embed author: {first_embed_author}",
            )
            await market_view_listener(self.bot, message)


# 🌈────────────────────────────────────────────
#        🛠️ Setup function to add cog to bot
# 🌈────────────────────────────────────────────
async def setup(bot: commands.Bot):
    await bot.add_cog(MessageCreateListener(bot))
