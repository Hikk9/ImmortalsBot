from discord.ext import commands
from asyncio.windows_events import NULL
import discord
from discord.ext.commands.errors import MissingAnyRole
from var import *


class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_any_role("Triumviri", "🤖 Signore dei Bot")
    async def rank(self, ctx):
        
        i = 2
        newname = ""
        oldname = ""
        k = 0
        embed = discord.Embed(title="Results", color=discord.Color.green(), inline=True)
        embed.set_thumbnail(url=img)
        embed.set_author(name="IMMORTAL BOT\n", icon_url=img)
        embed.set_footer(text="finished, thanks.")

        while i > 0: 
            for member in ctx.guild.members:
                aut = ctx.message.author.mention
                SpaceSplit = member.display_name.split(" ", 1)
                QuadraSplit = member.display_name.split("]", 1)
                boss = str(ctx.guild.owner)
                boss = boss.split("#")
                print(SpaceSplit)

                try:
                    if SpaceSplit[0].startswith("[") and SpaceSplit[0].endswith("]") and len(SpaceSplit) == 2:
                        for role in member.roles:
                            if member.name != boss[0]:
                                if str(role) == str(role) in ["@everyone", "Triumviri", "[I]Legato", "[II]Tribuno", "[III]Prefetto"]:  #"@everyone" or "Triumviri" or "[I]Legato" or "[II]Tribuno":
                                    NULL
                                else:
                                    y = 0
                                    
                                    for x in ruoli: 
                                        if str(role) == ruoli[y]:
                                            if SpaceSplit[0] != gradi[y]:
                                                tmp2 = gradi[y] + " " + SpaceSplit[1]

                                                oldname = oldname + f"{member.display_name}\n"
                                                newname = newname + f"{tmp2}\n"

                                                await member.edit(nick=tmp2)
                                        y+=1

                    elif len(SpaceSplit) == 2 and SpaceSplit[0].startswith("["):
                        print(SpaceSplit)
                        tmp2 = "[XI]" + " " + SpaceSplit[1]
                        oldname = oldname + f"{member.display_name}\n"
                        newname = newname + f"{tmp2}\n"
                        await member.edit(nick=tmp2)
                    elif len(SpaceSplit) == 2:
                        print(SpaceSplit)
                        tmp2 = "[XI]" + " " + SpaceSplit[0] + SpaceSplit[1]
                        oldname = oldname + f"{member.display_name}\n"
                        newname = newname + f"{tmp2}\n"
                        await member.edit(nick=tmp2)
                    elif len(QuadraSplit) == 2:
                        tmp2 = "[XI]" + " " + QuadraSplit[1]
                        oldname = oldname + f"{member.display_name}\n"
                        newname = newname + f"{tmp2}\n"
                        await member.edit(nick=tmp2)
                    else:
                        tmp2 = "[XI]" + " " + member.display_name
                        oldname = oldname + f"{member.display_name}\n"
                        newname = newname + f"{tmp2}\n"
                        await member.edit(nick=tmp2)
                except:
                    NULL
            print("-------------------------------------")
            print(oldname)
            i = i - 1
            if oldname and newname != "":
                oldname = oldname + "\n"
                newname = newname + "\n"

        print ("oldname len " + str(len(oldname)))
        print ("oldname len " + str(len(newname)))
        print(oldname)
        print(newname)

        if len(oldname) == len(newname) == 0:
            await ctx.send(f"No one name has been changed. {ctx.message.author.mention}")
        else:
            embed.add_field(name = "old names", value = oldname)
            embed.add_field(name = "new names", value = newname)
            #print(newname)
            #print("-------------------------------------")
            #print(oldname)
            print("finito")
            #FARE UN EMBED CON TUTTI I NOMI CAMBIATI PRIMA E DOPo
            await ctx.send(embed = embed)
            await ctx.send(ctx.message.author.mention)
    
    @rank.error
    async def info_error(self, ctx, error):
        if isinstance(error, MissingAnyRole):
            await ctx.send("don't have permission for this command")





def setup(bot):
    bot.add_cog(admin(bot))
