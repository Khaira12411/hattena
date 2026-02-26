import inspect

import discord

from straydex.AR.h import straydex_ar
from straydex.desc import type_info
from utils.logs.debug_log import debug_enabled, debug_log, enable_debug

enable_debug(f"{__name__}.send_response")
enable_debug(f"{__name__}.handle_straydex_command")
enable_debug(f"{__name__}.handle_exact_command")


async def send_response(message_or_interaction, response):
    """
    ✨ Sends a reply to a message or interaction without pinging the user ✨

    Parameters:
    - message_or_interaction: discord.Message or discord.Interaction
    - response: one of
       * tuple(embeds or embed, view, content)
       * tuple(embeds or embed, content)
       * list of embeds
       * single embed
       * string message
       * dict with 'embed' and 'content' keys
    """
    debug_log(f"{response}")
    # Choose the right send function depending on type
    if isinstance(message_or_interaction, discord.Message):

        async def send_func(**kwargs):
            debug_log(
                f"send_func (Message): id={getattr(message_or_interaction, 'id', None)}, kwargs={kwargs}"
            )
            await message_or_interaction.reply(mention_author=False, **kwargs)
            debug_log(
                f"Reply sent to Message: {getattr(message_or_interaction, 'id', None)}"
            )

    elif isinstance(message_or_interaction, discord.Interaction):
        responded = message_or_interaction.response.is_done()

        async def send_func(**kwargs):
            debug_log(
                f"send_func (Interaction): user={getattr(message_or_interaction, 'user', None)}, kwargs={kwargs}"
            )
            if not responded:
                await message_or_interaction.response.send_message(**kwargs)
                debug_log("Initial response sent to Interaction.")
            else:
                await message_or_interaction.followup.send(**kwargs)
                debug_log("Followup response sent to Interaction.")

    else:
        debug_log(
            f"TypeError: Expected discord.Message or discord.Interaction, got {type(message_or_interaction)}",
            highlight=True,
        )
        raise TypeError("Expected discord.Message or discord.Interaction")

    # Now send the response content
    debug_log(f"Preparing to send response of type: {type(response)}")
    if isinstance(response, tuple) and len(response) == 3:
        embeds_or_embed, view, content = response
        debug_log(
            f"Tuple (3): embeds_or_embed={embeds_or_embed}, view={view}, content={content}"
        )
        if isinstance(embeds_or_embed, list):
            await send_func(embeds=embeds_or_embed, view=view, content=content)
            debug_log("Sent list of embeds with view and content.")
        else:
            await send_func(embed=embeds_or_embed, view=view, content=content)
            debug_log("Sent single embed with view and content.")

    elif isinstance(response, tuple) and len(response) == 2:
        embeds_or_embed, content = response
        debug_log(f"Tuple (2): embeds_or_embed={embeds_or_embed}, content={content}")
        if isinstance(embeds_or_embed, list):
            await send_func(embeds=embeds_or_embed, content=content)
            debug_log("Sent list of embeds with content.")
        else:
            await send_func(embed=embeds_or_embed, content=content)
            debug_log("Sent single embed with content.")

    elif isinstance(response, dict) and "embed" in response and "content" in response:
        # New condition: dict with embed and content
        debug_log(f"Dict: embed={response['embed']}, content={response['content']}")
        await send_func(embed=response["embed"], content=response["content"])
        debug_log("Sent dict embed and content.")

    elif isinstance(response, list):
        debug_log(f"List of embeds: {response}")
        await send_func(embeds=response)
        debug_log("Sent list of embeds.")

    elif isinstance(response, discord.Embed):
        debug_log(f"Single embed: {response}")
        await send_func(embed=response)
        debug_log("Sent single embed.")

    elif isinstance(response, str):
        debug_log(f"String response: {response}")
        await send_func(content=response)
        debug_log("Sent string response.")

    else:
        debug_log(
            f"Unknown response type: {type(response)}, value: {response}",
            highlight=True,
        )
        await send_func(content=str(response))
        debug_log("Sent fallback string response.")


async def handle_straydex_command(
    guild: discord.Guild,
    message_content: str,
    bot,
    user_display_name: str,
    user_id: int,
    prefix="!",
):
    if not message_content.startswith(prefix):
        debug_log(
            f"Rejected: message does not start with prefix '{prefix}' | content: {message_content}"
        )
        return None  # Not a Straydex command 🛑

    content = message_content[len(prefix) :].lower().strip()
    debug_log(f"Straydex command content parsed: '{content}'")

    # Reject spaces (commands must be one word, e.g. !wbgri)
    if " " in content:
        debug_log(f"Rejected: command contains spaces | content: '{content}'")
        return None  # 🚫 Don't even try responding if spaces are there

    # Find the longest matching main command — but only if it's a real key in straydex_ar ✨
    matched_main = None
    for main_cmd in straydex_ar.keys():
        if content.startswith(main_cmd):
            if matched_main is None or len(main_cmd) > len(matched_main):
                matched_main = main_cmd
                debug_log(f"Matched main command: '{matched_main}'")

    # If we didn't find anything, stay silent like a ninja 🥷
    if not matched_main:
        debug_log(f"No matching main command found for content: '{content}'")
        debug_log(f"Current main commands: {list(straydex_ar.keys())}")
        return None

    # If the command is not exactly the main_cmd or main_cmd + valid sub_cmd, ignore it 🐾
    main_dict = straydex_ar[matched_main]
    sub_cmd = content[len(matched_main) :]
    debug_log(f"Subcommand parsed: '{sub_cmd}' for main command '{matched_main}'")

    # Strict check — sub_cmd must exist in dict (including "")
    if sub_cmd not in main_dict:
        debug_log(
            f"Rejected: subcommand '{sub_cmd}' not found in main_dict for '{matched_main}'"
        )
        return None

    # Get handler for subcommand
    handler = main_dict[sub_cmd]
    if not handler:
        debug_log(
            f"Rejected: handler not found for subcommand '{sub_cmd}' in main_dict for '{matched_main}'"
        )
        return None

    # Figure out the function & extra args 🎁
    if callable(handler):
        func = handler
        extra = {}
    elif isinstance(handler, dict):
        func = handler.get("function")
        extra = handler
    else:
        debug_log(
            f"Rejected: handler type not callable or dict for subcommand '{sub_cmd}'"
        )
        return None

    if not func:
        debug_log(f"Rejected: function not found in handler for subcommand '{sub_cmd}'")
        return None

    # Build kwargs based on function signature 🛠️
    params = inspect.signature(func).parameters
    kwargs = {"guild": guild, "user_display_name": user_display_name}

    if "user_id" in params:
        kwargs["user_id"] = user_id
    if "bot" in params:
        kwargs["bot"] = bot
    if "main_cmd" in params:
        kwargs["main_cmd"] = matched_main
    if "boss_name" in params:
        kwargs["boss_name"] = sub_cmd if sub_cmd else ""
    if "cmd" in params:
        kwargs["cmd"] = (
            content  # <-- Added this line to pass full command without prefix
        )

    if "text" in extra:
        kwargs["text"] = extra["text"]
    if "sub_cmd" in extra:
        kwargs["sub_cmd"] = extra["sub_cmd"]
    if "button_label" in extra:
        kwargs["button_label"] = extra["button_label"]
    if "button_emoji" in extra:
        kwargs["button_emoji"] = extra["button_emoji"]
    if "image_url" in extra:
        kwargs["image_url"] = extra["image_url"]
    if "patreon" in extra:
        kwargs["patreon"] = extra["patreon"]
    if "explore_map" in extra:
        kwargs["explore_map"] = extra["explore_map"]
    if "image_url_second" in extra:
        kwargs["image_url_second"] = extra["image_url_second"]
    if "text_second" in extra:
        kwargs["text_second"] = extra["text_second"]
    if "thumbnail_url" in extra:
        kwargs["thumbnail_url"] = extra["thumbnail_url"]
    # Call the magic function ✨
    debug_log(f"Calling handler function '{func.__name__}' with kwargs: {kwargs}")
    response = await func(**kwargs)
    debug_log(f"Handler function '{func.__name__}' returned response: {response}")
    return response


async def handle_exact_command(
    guild: discord.Guild,
    message_content: str,
    bot,
    user_display_name: str,
    user_id: int,
    prefix="!",
):
    """
    Handles commands that require an exact match to a known command or type.
    Examples: "!amuletcoin", "!firestone", "!bug" (type)

    Steps:
    1. Check if message starts with prefix.
    2. Extract command content (lowercased).
    3. If content matches a type (like "bug", "fire"), call its function with type info.
    4. Else if content matches a command key exactly in straydex_ar, call its function.
    5. Otherwise, return None.

    To add a new unique type command:
    - Add the type to `type_info` with required data and a "function" key for the embed builder.
    - The function should accept kwargs like "thumbnail", "image", "color" if needed.
    """
    if not message_content.startswith(prefix):
        debug_log(
            f"Rejected: message does not start with prefix '{prefix}' | content: {message_content}"
        )
        return None

    content = message_content[len(prefix) :].lower().strip()
    debug_log(f"Exact command content parsed: '{content}'")

    # Handle type commands first (e.g., !bug, !fire)
    if content in type_info:
        debug_log(f"Matched type command: '{content}' in type_info")
        type_data = type_info[content]
        func = type_data.get("function")
        if not func:
            debug_log(f"Rejected: function not found in type_data for '{content}'")
            return None

        params = inspect.signature(func).parameters
        kwargs = {"guild": guild, "user_display_name": user_display_name}
        if "user_id" in params:
            kwargs["user_id"] = user_id
        if "bot" in params:
            kwargs["bot"] = bot
        if "main_cmd" in params:
            kwargs["main_cmd"] = content
        if "thumbnail_url" in params:
            kwargs["thumbnail_url"] = type_data.get("thumbnail")
        if "image_url" in params:
            kwargs["image_url"] = type_data.get("image")
        if "color" in params:
            kwargs["color"] = type_data.get("color")

        debug_log(
            f"Calling type command function '{func.__name__}' with kwargs: {kwargs}"
        )
        response = await func(**kwargs)
        debug_log(
            f"Type command function '{func.__name__}' returned response: {response}"
        )
        return response

    # Otherwise, check for exact command match in straydex_ar
    if content not in straydex_ar:
        debug_log(f"Rejected: exact command '{content}' not found in straydex_ar")
        return None

    item_data = straydex_ar.get(content)
    if not item_data:
        debug_log(f"Rejected: item_data not found for exact command '{content}'")
        return None

    func = item_data.get("function")
    if not func:
        if content in type_info:
            debug_log(f"type_data for '{content}': {type_info[content]}")
        debug_log(
            f"Rejected: function not found in item_data for exact command '{content}'"
        )
        return None

    params = inspect.signature(func).parameters
    kwargs = {"guild": guild, "user_display_name": user_display_name}
    if "user_id" in params:
        kwargs["user_id"] = user_id
    if "bot" in params:
        kwargs["bot"] = bot
    if "main_cmd" in params:
        kwargs["main_cmd"] = content
    if "text" in item_data:
        kwargs["text"] = item_data["text"]
    if "image_url" in item_data:
        kwargs["image_url"] = item_data["image_url"]

    debug_log(f"Calling exact command function '{func.__name__}' with kwargs: {kwargs}")
    response = await func(**kwargs)
    debug_log(f"Exact command function '{func.__name__}' returned response: {response}")
    return response


# ---------------------------
# How to add a new unique type:
#
# 1. Add a new key in your `type_info` dictionary:
#    - Include keys "thumbnail", "image", "color"
#    - Add "function": the function that builds the embed for this type
#
# 2. Implement the embed function if it doesn't exist.
#    It should accept the kwargs you plan to send, e.g., guild, thumbnail, image, color, etc.
#
# 3. The handler automatically detects the new type based on the `content` string.
#
# Example:
# type_info["newtype"] = {
#     "thumbnail": "url_to_thumbnail_image",
#     "image": "url_to_large_image",
#     "color": 123456,
#     "function": build_newtype_embed_function,
# }
#
# Then just ensure build_newtype_embed_function is async and accepts appropriate kwargs.
# }
#
# Then just ensure build_newtype_embed_function is async and accepts appropriate kwargs.
