import discord
from discord import app_commands
from discord.ext import commands

from constants.aesthetic import Emojis
from utils.db.straydex_guild import upsert_straydex_guild
from utils.functions.webhook import send_webhook
from utils.logs.pretty_log import pretty_log
from utils.visuals.pretty_defer import pretty_defer
from constants.straymons_constants import STRAYMONS__TEXT_CHANNELS, STRAYMONS_GUILD_ID

class SetUpdateChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="set-update-channel",
        description="Set the channel for Straydex update notifications in this guild.",
    )
    # Only allow users with Manage Guild permissions to use this command
    @app_commands.checks.has_permissions(manage_guild=True)
    @app_commands.describe(
        channel="The channel to receive Straydex update notifications.",
    )
    async def set_update_channel(
        self, interaction: discord.Interaction, channel: discord.TextChannel
    ):
        guild_id = interaction.guild_id
        guild_name = interaction.guild.name
        update_channel_id = channel.id
        update_channel_name = channel.name

        loader = await pretty_defer(
            interaction=interaction,
            content=f"Setting {channel.mention} as the Straydex update channel...",
            ephemeral=False,
        )

        # Update the database with the new channel information
        try:
            await upsert_straydex_guild(
                bot=self.bot,
                guild_id=guild_id,
                guild_name=guild_name,
                update_channel_id=update_channel_id,
                update_channel_name=update_channel_name,
            )
            content = f"Successfully set {channel.mention} as the Straydex update channel for this guild."
            await loader.success(content=content)

            desc = (
                f"Guild: {guild_name}\n"
                f"Channel: {channel.name}\n"
                f"Set by: {interaction.user.mention}"
            )
            log_embed = discord.Embed(
                title="Straydex Update Channel Set",
                description=desc,
                color=discord.Color.green(),
            )
            log_embed.set_author(
                name=interaction.user.display_name,
                icon_url=interaction.user.display_avatar.url,
            )
            log_embed.set_thumbnail(url=interaction.guild.icon.url if interaction.guild.icon else None)
            log_embed.set_footer(
                text=f"Guild ID: {guild_id} | Channel ID: {update_channel_id}",
                icon_url=interaction.guild.icon.url if interaction.guild.icon else None,
            )
            straymons_guild = self.bot.get_guild(STRAYMONS_GUILD_ID)
            straymons_bot_log_channel = straymons_guild.get_channel(STRAYMONS__TEXT_CHANNELS.bot_logs)
            await send_webhook(
                bot=self.bot,
                channel=straymons_bot_log_channel,
                content="",
                embed=log_embed,
            )

        except Exception as e:
            await loader.edit(content=f"Failed to set update channel: {e}")
            return
    set_update_channel.extras = {"category": "Staff"}

async def setup(bot):
    await bot.add_cog(SetUpdateChannel(bot))