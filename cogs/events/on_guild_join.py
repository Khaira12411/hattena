import discord
from discord.ext import commands
from constants.straymons_constants import STRAYMONS__TEXT_CHANNELS
TEMP_LOG_CHANNEL_ID = STRAYMONS__TEXT_CHANNELS.bot_logs
from constants.aesthetic import Emojis
from utils.logs.pretty_log import pretty_log

async def send_guild_join_message(bot, guild):
    content = (
        f"{Emojis.blue_flower_two} Hello! Thanks for inviting me to **{guild.name}**! I'm Hatenna, a bot designed to provide Straydex related features and updates.\n\n"
        f"To get started, please type `!h` to see a list of available straydex commands.\n"
        f"To get Straydex updates, please set up a channel for me to post in using the `/set-update-channel` command."
    )

    # Find a channel where hatenna has permission to send messages
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            try:
                await channel.send(content)
                break
            except Exception as e:
                pretty_log("error", f"Failed to send guild join message in {guild.name} ({guild.id}): {e}")

class OnGuildJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        log_embed = discord.Embed(
            title="Joined New Guild",
            description=f"**Guild Name:** {guild.name}\n**Guild ID:** {guild.id}\n**Member Count:** {guild.member_count}\n**Owner:** {guild.owner} ({guild.owner_id})",
            color=discord.Color.green(),
        )
        log_embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        log_channel = self.bot.get_channel(TEMP_LOG_CHANNEL_ID)
        if log_channel:
            await log_channel.send(embed=log_embed)

        await send_guild_join_message(self.bot, guild)


async def setup(bot):
    await bot.add_cog(OnGuildJoin(bot))
