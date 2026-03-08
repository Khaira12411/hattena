SKIP_FIRST_GUILD = False  # Set to False to send to all guilds
import discord
from discord import app_commands
from discord.ext import commands

from constants.aesthetic import Emojis
from constants.straymons_constants import DEFAULT_EMBED_COLOR, STRAYMONS_GUILD_ID
from utils.cache.straydex_guild_cache import (
    fetch_all_straydex_guild_w_update_channel_cache,
)
from utils.functions.webhook import send_webhook
from utils.logs.debug_log import debug_enabled, debug_log, enable_debug
from utils.logs.pretty_log import pretty_log
from utils.visuals.pretty_defer import pretty_defer

enable_debug(f"{__name__}.straydex_update_log")
enable_debug(f"{__name__}.on_submit")


class ChangeLogModal(discord.ui.Modal, title="Straydex Update Log"):
    log_content = discord.ui.TextInput(
        label="Update Log Content",
        style=discord.TextStyle.paragraph,
        placeholder="Enter the content for the Straydex update log message.",
        required=True,
        max_length=2000,
    )

    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    async def on_submit(self, interaction: discord.Interaction):
        debug_log(
            f"[StraydexUpdateLog] Modal submitted by user {interaction.user} (ID: {interaction.user.id})"
        )
        loader = await pretty_defer(
            interaction=interaction,
            content="Sending Straydex update log...",
            ephemeral=True,
        )

        log_message = self.log_content.value
        debug_log(f"[StraydexUpdateLog] Log message: {log_message}")
        pretty_log(
            "info",
            f"Received new Straydex update log content from {interaction.user} (ID: {interaction.user.id}): {log_message}",
            label="Straydex Update Log",
        )

        # Build the embed for the update log
        embed = discord.Embed(
            title=f"{Emojis.blue_flower_two} Straydex Update",
            description=log_message,
            color=DEFAULT_EMBED_COLOR,
        )

        # Fetch all guilds with update channels from cache
        guilds_with_channels = fetch_all_straydex_guild_w_update_channel_cache()
        debug_log(f"[StraydexUpdateLog] guilds_with_channels: {guilds_with_channels}")
        pretty_log(
            "info",
            f"Fetched {len(guilds_with_channels)} guild(s) with Straydex update channels from cache.",
            label="Straydex Update Log",
        )

        if not guilds_with_channels:
            debug_log("[StraydexUpdateLog] No guilds with update channels found.")
            await loader.error(
                content="No guilds have a Straydex update channel set. Please set up an update channel in at least one guild to use this command."
            )
            return

        updated_guilds = []  # moved outside loop

        # Optionally skip the first guild (for testing/debugging)

        guilds_list = list(guilds_with_channels.values())
        if SKIP_FIRST_GUILD:
            guilds_list = guilds_list[1:]

        # Send the update log to each guild's designated channel
        for guild_info in guilds_list:
            channel_id = guild_info["update_channel_id"]
            channel_name = guild_info["update_channel_name"]
            debug_log(
                f"[StraydexUpdateLog] Attempting to get channel for ID: {channel_id} (name: {channel_name})"
            )
            try:
                # Try cache first
                channel = self.bot.get_channel(channel_id)
                debug_log(
                    f"[StraydexUpdateLog] get_channel({channel_id}) returned: {channel}"
                )
                if channel is None:
                    try:
                        channel = await self.bot.fetch_channel(channel_id)
                        debug_log(
                            f"[StraydexUpdateLog] fetch_channel({channel_id}) returned: {channel}"
                        )
                        pretty_log(
                            "debug",
                            f"Fetched channel {channel_name} (ID: {channel_id}) from API.",
                            label="Straydex Update Log",
                        )
                    except Exception as e:
                        debug_log(
                            f"[StraydexUpdateLog] Exception in fetch_channel({channel_id}): {e}"
                        )
                        pretty_log(
                            "error",
                            f"Failed to fetch channel with ID {channel_id} for guild '{guild_info['guild_name']}' (ID: {guild_info['guild_id']}): {e}",
                            label="Straydex Update Log",
                        )
                        continue

                if channel:
                    try:
                        debug_log(
                            f"[StraydexUpdateLog] Attempting to send update log to channel: {channel} (ID: {channel_id})"
                        )
                        pretty_log(
                            "debug",
                            f"Attempting to send update log to channel '{channel_name}' (ID: {channel_id}) in guild '{guild_info['guild_name']}'...",
                            label="Straydex Update Log",
                        )
                        await channel.send(embed=embed)
                        debug_log(
                            f"[StraydexUpdateLog] Successfully sent update log to channel: {channel} (ID: {channel_id})"
                        )
                        pretty_log(
                            "info",
                            f"Sent Straydex update log to channel '{channel_name}' (ID: {channel_id}) in guild '{guild_info['guild_name']}' (ID: {guild_info['guild_id']}).",
                            label="Straydex Update Log",
                        )
                        updated_guilds.append(guild_info["guild_name"])
                    except Exception as e:
                        debug_log(
                            f"[StraydexUpdateLog] Exception while sending to channel {channel_id}: {e}"
                        )
                        pretty_log(
                            "error",
                            f"Failed to send Straydex update log to channel '{channel_name}' (ID: {channel_id}) in guild '{guild_info['guild_name']}' (ID: {guild_info['guild_id']}): {e}",
                            label="Straydex Update Log",
                        )
                        continue
                else:
                    debug_log(
                        f"[StraydexUpdateLog] Could not resolve channel with ID {channel_id}"
                    )
                    pretty_log(
                        "info",
                        f"Could not resolve channel with ID {channel_id} for guild '{guild_info['guild_name']}' (ID: {guild_info['guild_id']}). Skipping.",
                        label="Straydex Update Log",
                    )
                    continue

            except Exception as e:
                pretty_log(
                    "error",
                    f"Unexpected error while processing guild '{guild_info['guild_name']}' (ID: {guild_info['guild_id']}): {e}",
                    label="Straydex Update Log",
                )
                continue

        if updated_guilds:
            await loader.success(
                content=f"Straydex update log sent to {len(updated_guilds)} guild(s): {', '.join(updated_guilds)}"
            )
        else:
            await loader.error(content="Failed to send update log to any guilds.")


class StraydexUpdateLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="straydex-update-log",
        description="Send an update log message to all guilds with a Straydex update channel set.",
    )
    @app_commands.guilds(discord.Object(id=STRAYMONS_GUILD_ID))  # Straymons Guild ID
    async def straydex_update_log(self, interaction: discord.Interaction):
        try:
            # Set skip_first_guild=True to skip the first guild, False to send to all
            modal = ChangeLogModal(self.bot)
            # Pass skip_first_guild as needed (set to True to skip first guild)
            await interaction.response.send_modal(modal)
            # To actually use the flag, you would need to modify how the modal is submitted/handled.
            # For now, the flag is available in on_submit, set to False by default.
        except Exception as e:
            pretty_log(
                "error",
                f"Failed to send Straydex update log modal to {interaction.user} (ID: {interaction.user.id}): {e}",
                label="Straydex Update Log",
            )
            await interaction.response.send_message(
                content="An error occurred while trying to send the update log modal. Please try again later.",
                ephemeral=True,
            )

    straydex_update_log.extras = {"category": "Khy"}


async def setup(bot):
    await bot.add_cog(StraydexUpdateLog(bot))
