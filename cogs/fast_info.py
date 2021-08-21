from asyncio.windows_events import NULL
from sys import float_info
import discord
from discord import colour
from dislash import *
from discord.ext import commands
from discord.utils import get
from vars.command_desc import *


class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command()
    async def f(self, ctx, *,menu = None):
        if menu == None:
            embed = discord.Embed(colour = discord.Colour.red(), title = "incorrect title")
            embed.add_field(name=" \u200b \nComando non completo", value="per usare correttamente usa: \n \u200b \n > .f info" )
            await ctx.send(embed = embed)
        elif menu == "spada":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_sword)
        elif menu == "stocco":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_rapier)
        elif menu == "accette":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_hatchet)
        elif menu == "lancia":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_spear)
        elif menu == "ascia":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_great_axe)
        elif menu == "martello":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_war_hammer)
        elif menu == "arco":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_bow)
        elif menu == "moschetto":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_musket)
        elif menu == "staffa fuoco":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_fire_staff)
        elif menu == "staffa vita":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_life_staff)
        elif menu == "guanto ghiaccio":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            embed.add_field(name="Mod help Menu", value="menu")
            await ctx.send(embed = embed_ice_gauntlet)
        elif menu == "info":
            embed = discord.Embed(colour = discord.Colour.green(), title = "incorrect title")
            armi = "usare il comando `.f` e il nome di una delle seguenti armi:\n"
            index = 0
            for x in f_info:
                armi += f"> {f_info[index]}\n"
                index += 1
            embed.add_field(name="Info help menu", value= armi)
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(colour = discord.Colour.red(), title = "incorrect title")
            embed.add_field(name=" \u200b \nComando non corretto", value="per usare correttamente: \n \u200b \n > .f nome_arma \n > .f info \u200b \n \u200b \n esempio: \n > `.f lancia` \n > `.f info`")
            await ctx.send(embed = embed)



def setup(bot):
    bot.add_cog(commands(bot))
