from discord.ext import commands
import discord
from discord.ext.commands.errors import MissingAnyRole
from vars import *
class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_any_role("Triumviri", "Hik")
    @commands.command(pass_context=True)
    async def chnick(self, ctx, member: discord.Member, nickame):
        await member.edit(nick=nickame)
        await ctx.send(f'Nickname was changed from {member.display_name} to {member.mention} ')

    @chnick.error
    async def info_error(self, ctx, error):
        if isinstance(error, MissingAnyRole):
            await ctx.send("don't have permission for this command")

def setup(bot):
    bot.add_cog(commands(bot))
