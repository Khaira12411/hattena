import discord
from discord.ext import commands
from constants.straymons_constants import STRAYMONS__TEXT_CHANNELS
TEMP_LOG_CHANNEL_ID = STRAYMONS__TEXT_CHANNELS.bot_logs


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


async def setup(bot):
    await bot.add_cog(OnGuildJoin(bot))
