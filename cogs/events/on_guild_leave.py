import discord
from discord import app_commands
from discord.ext import commands
from utils.db.straydex_guild import remove_straydex_guild
from utils.logs.pretty_log import pretty_log

class OnGuildLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_leave(self, guild):
        guild_id = guild.id
        guild_name = guild.name

        # Remove the guild from the database
        try:
            await remove_straydex_guild(bot=self.bot, guild_id=guild_id)
            pretty_log(
                "guild",
                f"Left guild '{guild_name}' (ID: {guild_id}). Removed from Straydex guilds database.",
            )
        except Exception as e:
            pretty_log(
                "error",
                f"Failed to remove guild '{guild_name}' (ID: {guild_id}) from database on leave: {e}",
            )
async def setup(bot):
    await bot.add_cog(OnGuildLeave(bot))