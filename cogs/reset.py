from discord.ext import commands
from asyncio.windows_events import NULL
import asyncio

from discord.ext.commands.errors import MissingAnyRole
from var import *
class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("Triumviri", "Hik")
    async def reset(self, ctx):
        boss = str(ctx.guild.owner)
        boss = boss.split("#")
        msg = await ctx.send("Are you sure to reset all nicknames?")
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")


        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) in ['✅', '❌']

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=3, check=check)
            
            if reaction.emoji == '✅':
                #await  msg.delete()
                print("a")
                
                await msg.edit(content="Are you REALLY sure to reset?")

                await msg.add_reaction("✅")
                await msg.add_reaction("❌")

                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) in ['✅', '❌']

                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=3, check=check)

                except asyncio.TimeoutError:
                    await ctx.send("I know, you're not sure, come back later.")
                    await msg.delete()
                    return
                
                if reaction.emoji == '✅':
                    await  msg.delete()
        
                    for member in ctx.guild.members:
                            for role in member.roles:
                                if member.name != boss[0]:
                                    if str(role) == str(role) in ["@everyone", "Triumviri", "[I]Legato", "[II]Tribuno", "[III]Tribuno"]:  #"@everyone" or "Triumviri" or "[I]Legato" or "[II]Tribuno":
                                        NULL
                                    else:
                                            await member.edit(nick=member.name)
                    await ctx.send("{}, you did it.".format(ctx.message.author.mention))


                elif reaction.emoji == '❌':
                    await ctx.send("ha! too scared")
                    await  msg.delete()
                    return

            elif reaction.emoji == '❌':
                await ctx.send("ha! too scared")
                await  msg.delete()
                return

        except asyncio.TimeoutError:
            await ctx.send("Too slow")
            await  msg.delete()
            return
            
    @reset.error
    async def info_error(self, ctx, error):
        if isinstance(error, MissingAnyRole):
            await ctx.send("don't have permission for this command")               




def setup(bot):
    bot.add_cog(admin(bot))
