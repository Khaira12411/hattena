import asyncio
import re

import discord
from discord.ext import commands

from constants.ask_hattena.overall import TOPICS
from constants.straymons_constants import PREFIX
from utils.functions.ability_moves_lookup import ability_moves_lookup
from utils.functions.ask_hattena import match_topic
from utils.listener_func.straydex_handler import straydex_command_handler
from utils.logs.pretty_log import pretty_log


async def mention_listener(bot: commands.Bot, message: discord.Message):

    content = message.content.lower()
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
        r"weakness ([\w\-'. ]+)",  # Added pattern for 'weakness pokemon'
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
                bot=bot,
                message=message,
                cmd=topic_cmd,
            )
        except Exception as e:
            pretty_log(
                "error",
                f"Error handling Straydex command for topic '{topic}': {e}",
                include_trace=True,
            )

    content = content.replace(f"<@{bot.user.id}>", "").strip()
    content = content.replace(f"<@!{bot.user.id}>", "").strip()

    # --- Custom ability/moves pattern ---
    # New pattern: @<this bot> lookup pokemon/mon <ability> <moves...>
    lookup_pattern = re.compile(
        r"<@!?(?P<bot_id>\d+)>\s+lookup\s+(?:pokemon|mon)\s+([\w\- ]+?)\s+([\w\- ]+.*)"
    )

    match = lookup_pattern.search(message.content)
    if match:
        # Only proceed if the mention matches THIS bot's ID
        if int(match.group("bot_id")) == bot.user.id:
            ability = match.group(2).strip()
            moves = match.group(3).strip().replace(",", " ").replace(";", " ")
            move_list = [m for m in moves.split() if m]
            pretty_log(
                "debug",
                f"Calling ability_moves_lookup with ability='{ability}', moves={move_list}",
                label="MentionListener",
            )
            try:
                await ability_moves_lookup(message, ability, move_list)
                pretty_log(
                    "debug", "Returned from ability_moves_lookup", label="MentionListener"
                )
            except Exception as e:
                pretty_log(
                    "error",
                    f"Error in ability_moves_lookup: {e}",
                    include_trace=True,
                    label="MentionListener",
                )
                await message.reply(
                    f"Sorry, I had trouble looking up that ability and moves. Please make sure the format is correct and try again."
                )
            return
