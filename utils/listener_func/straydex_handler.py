import discord

from straydex.functions.response import handle_exact_command, send_response, handle_straydex_command
from utils.logs.pretty_log import pretty_log
from straydex.functions.main import send_sd_logs

async def straydex_command_handler(
    bot: discord.Client,
    message: discord.Message,
):
    """Handles Straydex-related commands based on message content."""
    guild = message.guild
    try:
        response = await handle_exact_command(
            guild=guild,
            message_content=message.content,
            bot=bot,
            user_display_name=message.author.display_name,
            user_id=message.author.id,
        )

        if not response:
            response = await handle_straydex_command(
                guild=guild,
                message_content=message.content,
                bot=bot,
                user_display_name=message.author.display_name,
                user_id=message.author.id,
            )
    except Exception as e:
        pretty_log(
            tag="error",
            message=f"Error processing Straydex command: {e}",
            include_trace=True,
        )
        response = None
        
    if response:
        try:
            await send_response(message, response)

            # Log the command usage
            main_cmd = message.content.lower().strip()
            await send_sd_logs(
                bot=bot,
                main_cmd=main_cmd,
                user=message.author,
                channel=message.channel,
            )

        except Exception as e:
            pretty_log(
                tag="error",
                message=f"Error sending Straydex response: {e}",
                include_trace=True,
            )