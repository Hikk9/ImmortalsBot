from asyncio.windows_events import NULL
from inspect import getblock
import time
from typing import Text
from discord.ext.commands.errors import CommandNotFound
from dislash import *
from discord.ext import commands
from discord.utils import get
from command_desc import *
from wepembed import *
from var import *
from var import current_line

tmp = "main_info_page"
msg = ""
msg2 = ""
page = page_1
lista = main_info_page
class commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            print("yep")

    @commands.command()
    async def s(self, ctx):
        global msg
        msg = await ctx.send(
            "Selezione l'arma di cui vuoi informazioni",
            components=[
                SelectMenu(
                    custom_id="test",
                    placeholder="Seleziona un opzione",
                    max_values=1,
                    options=[
                        SelectOption("Spada e Scudo", "Spada e Scudo"),
                        SelectOption("Stocco", "Stocco"),
                        SelectOption("Accette", "Accette"),
                        SelectOption("Lancia", "Lancia"),
                        SelectOption("Ascia bipenne", "Ascia bipenne"),
                        SelectOption("Martello da guerra", "Martello da guerra"),
                        SelectOption("Arco", "Arco"),
                        SelectOption("Moschetto", "Moschetto"),
                        SelectOption("Staffa del fuoco", "Staffa del fuoco"),
                        SelectOption("Staffa della vita", "Staffa della vita"),
                        SelectOption("Guanto del ghiaccio", "Guanto del ghiaccio")
                    ]
                )
            ]
        )
        # Wait for someone to click on it
    @commands.Cog.listener()
    async def on_dropdown(self, inter : MessageInteraction):
        global msg
        x = len(weapon_page)
        print(x)
        tmp = (inter.select_menu.selected_options[0].value)
        
        for x in weapon_page:
            if inter.select_menu.selected_options[0].value == x:
                print(f"tmp: {x}")
                if x == embed_sword: 
                    await msg.edit(content = "", embed = embed_sword, components = [])
                if x == "Spada e Scudo": await msg.edit(content = "", embed = embed_sword, components = [])
                if x == "Stocco": await msg.edit(content = "", embed = embed_rapier, components = [])
                if x == "Accette": await msg.edit(content = "", embed = embed_hatchet, components = [])
                if x == "Lancia": await msg.edit(content = "", embed = embed_spear, components = [])
                if x == "Ascia bipenne": await msg.edit(content = "", embed = embed_great_axe, components = [])
                if x == "Martello da guerra": await msg.edit(content = "", embed = embed_war_hammer, components = [])
                if x == "Arco": await msg.edit(content = "", embed = embed_bow, components = [])
                if x == "Moschetto": await msg.edit(content = "", embed = embed_musket, components = [])
                if x == "Staffa del fuoco": await msg.edit(content = "", embed = embed_fire_staff, components = [])
                if x == "Staffa della vita": await msg.edit(content = "", embed = embed_life_staff, components = [])
                if x == "Guanto del ghiaccio": await msg.edit(content = "", embed = embed_ice_gauntlet, components = [])
        
        #labels = [option.label for option in inter.select_menu.selected_options]
        #await inter.reply(f"Options: {', '.join(labels)}")




#--------------------------------------------------------


    @commands.command()
    async def help(self, ctx):
        global page
        page = page_1

        def show_lines(current_line, lines):
            
            text = ""
            for index, line in enumerate(lines):
                if index == current_line:
                    text += f"> {line}\n"
                else:
                    text += f"{line}\n"
            return text

        embed_main_info = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
        embed_main_info.set_author(name="IMMORTALS BOT\n", icon_url=img)
        embed_main_info.add_field(name = '\u200b', value=show_lines(current_line, main_info_page))

        def show_page(current_line, lines):
            global page,tmp
            print(f"tmp: {tmp}")
            text = ""
            for index, line in enumerate(lines):
                if index == current_line + 1:
                    if "main_info_page" in line:
                        page = page_1
                    elif "admin_command_page" in line:
                        page = page_2
                    elif "user_command_page" in line:
                        page = page_3
                    text = line
            return text
        
        def back_page(current_line, list):
            global page
            text = ""
            # list = weapon_page
            if "main_info_page" in page:
                page = page_1
                text = page[0]

            elif "admin_command_page" == page[0] and (tmp in admin_command_page):
                print(page)
                page = page_2
                text = page[0]
            elif "admin_command_page" == page[0] and not(tmp in admin_command_page):
                page = page_1
                text = page[0]

            elif "user_command_page" == page[0] and (tmp in user_command_page):
                print(page)
                page = page_3
                text = page[0]
            elif "user_command_page" == page[0] and not(tmp in user_command_page):
                page = page_1
                text = page[0]
            return text

            

        msg2 = await ctx.send(embed = embed_main_info, components=[info_row_1, info_row_2])
        on_click = msg2.create_click_listener(timeout=40)
        
        @on_click.not_from_user(ctx.author, cancel_others=True, reset_timeout=False)
        async def on_wrong_user(inter):
            # Reply with a hidden message
            await inter.reply("You're not the author", ephemeral=True)


        @on_click.matching_id("up")
        async def on_up(inter):
            global current_line,lista
            if current_line == 0:
                current_line = len(lista) - 1
            else:
                current_line = (current_line - 1) % len(lista)

        @on_click.matching_id("down")
        async def on_down(inter):
            global current_line,lista
            if current_line == (len(lista) - 1):
                current_line = 0
            else:
                current_line = (current_line + 1) % len(lista)

        @on_click.matching_id("enter")
        async def enter(inter):
            global current_line, tmp, lista
            cl = current_line
            current_line = 0
            tmp = show_page(cl, page)

        @on_click.matching_id("back")
        async def back(inter):
            global current_line ,main_info_page, tmp
            tmp = back_page(current_line, page)
            current_line = 0
        
        @on_click.no_checks()
        async def on_any_click(inter):
            global tmp,lista,current_line,components, page, embed_main_info
            # On any click from author (because otherwise this function would be canceled)
            if tmp == "main_info_page":
                lista = main_info_page
                embed_main_info.clear_fields()
                embed_main_info.add_field(name = '\u200b', value=show_lines(current_line, main_info_page))
                await inter.reply(type=7, embed=embed_main_info, components=[info_row_1,info_row_2])
            if tmp == "admin_command_page":
                a = ""
                for role in ctx.author.roles:
                    if str(role) == str(role) in ["Triumviri", "[I]Legato", "[II]Tribuno", "[III]Tribuno", "Hik"]:
                        a = 1
                        break
                    else:
                        a = 0
                if a == 1:
                    lista = admin_command_page
                    embed_main_info.clear_fields()
                    embed_main_info.add_field(name = '\u200b', value=show_lines(current_line, admin_command_page))
                    await inter.reply(type=7, embed=embed_main_info, components=[info_row_1,info_row_2])
                else:
                    embed_main_info.clear_fields()
                    embed_main_info.add_field(name = '\u200b', value="non hai accesso a questi comandi")
                    await inter.reply(type=7, embed= embed_main_info, components=[disabled_info_row_1,disabled_info_row_2])

            if tmp == "user_command_page":
                lista = user_command_page
                embed_main_info.clear_fields()
                embed_main_info.add_field(name = '\u200b', value=show_lines(current_line, user_command_page))
                await inter.reply(type=7, embed=embed_main_info, components=[info_row_1,info_row_2])
            if tmp == ".reset":
                embed_main_info.clear_fields()
                embed_main_info.add_field(name = 'Reset', value=reset_value)
                await inter.reply(type=7, embed= embed_main_info, components=[disabled_info_row_1,disabled_info_row_2])
                #await inter.reply(embed=embed_main_info)
            if tmp == ".rank":
                embed_main_info = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
                embed_main_info.set_author(name="IMMORTAL BOT\n", icon_url=img)
                embed_main_info.add_field(name = 'Rank', value=rank_value)
                await inter.reply(type=7, embed= embed_main_info, components=[disabled_info_row_1,disabled_info_row_2])
                #await inter.reply(embed=embed_main_info)
            if tmp == ".vrole":
                embed_main_info = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
                embed_main_info.set_author(name="IMMORTAL BOT\n", icon_url=img)
                embed_main_info.add_field(name = 'Vrole', value=vrole_value)
                await inter.reply(type=7, embed= embed_main_info, components=[disabled_info_row_1,disabled_info_row_2])
                #await inter.reply(embed=embed_main_info)
            if tmp == ".f":
                embed_main_info = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
                embed_main_info.set_author(name="IMMORTAL BOT\n", icon_url=img)
                embed_main_info.add_field(name = 'Visualizzazione Armi', value=f_value)
                await inter.reply(type=7, embed= embed_main_info, components=[disabled_info_row_1,disabled_info_row_2])
                #await inter.reply(embed=embed_main_info)

        @on_click.timeout
        async def on_timeout():
            global tmp
            tmp = "main_info_page"
            embed_main_info.clear_fields()
            embed_main_info.add_field(name = '\u200b', value= "".join(main_info_page))
            await msg2.delete()







def setup(bot):
    bot.add_cog(commands(bot))
