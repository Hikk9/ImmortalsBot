import asyncio
from asyncio.windows_events import NULL
import discord
from discord.embeds import EmbedProxy
from discord.ext import commands
from vars.var import *
from discord.ext.commands import MissingAnyRole

class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vrole(self, ctx):
        embed = discord.Embed(title="\u200b", color=discord.Color.green(), inline=True)
        embed.set_thumbnail(url=img)
        embed.set_author(name="IMMORTAL BOT\n", icon_url=img)
        embed.set_footer(text="LASCIAR FINIRE DI FAR AGGIUNGERE LE REACTION")
        embed.add_field(name = "Ruoli", value = ruoliembed)

        msg = await ctx.send(embed = embed)
        tmp = ""
        x = 10
        for c in range(x):
            await msg.add_reaction(emoji_numbers[c])
        def check(reaction, user):
                return user == ctx.message.author and str(reaction.emoji) in ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
                    
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=20, check=check)
            if emoji_numbers.index(reaction.emoji) or reaction.emoji == '0️⃣':
                embed.clear_fields()
                for member in ctx.guild.members:
                    for role in member.roles:
                        if str(role) == ruoli2[emoji_numbers.index(reaction.emoji)]:
                            tmp = tmp + f"\u200b \n {member.display_name} \n"
                if tmp != "":
                    embed.set_footer()
                    embed.add_field(name = f"membri con ruolo {ruoli2[emoji_numbers.index(reaction.emoji)]}", value = tmp, inline=True)
                    await msg.clear_reactions()
                    await msg.edit(embed = embed)
                    
                else:
                    await ctx.send(f"nessun membro ha questo ruolo. {ruoli2[emoji_numbers.index(reaction.emoji)]}")

        
                                                                                                                                                                                                             

        except asyncio.TimeoutError:
            await msg.delete()
            return  


def setup(bot):
    bot.add_cog(commands(bot))


