import discord
from dislash import *



weapon_page = [
    "Spada e Scudo",
    "Stocco",
    "Accette",
    "Lancia",
    "Ascia bipenne",
    "Martello da guerra",
    "Arco",
    "Moschetto",
    "Staffa del fuoco",
    "Staffa della vita",
    "Guanto del ghiaccio"
]
f_info = [
    "spada",
    "stocco",
    "accette",
    "lancia",
    "ascia",
    "martello",
    "arco",
    "moschetto",
    "staffa fuoco",
    "staffa vita",
    "guanto ghiaccio"
]


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_sword = discord.Embed(title="Info Spada e Scudo", color=discord.Color.green(), inline=True)
embed_sword.set_thumbnail(url="attachment://spear.jpg")
#embed_wordr.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_sword.add_field(name = 'Scaling', value= f"> destrezza: `0.65` \n > forza: `0.9`", inline = False)
embed_sword.add_field(name = 'Tipo di danno', value = "> Taglio", inline = False)
embed_sword.add_field(name = 'example', value = "exampl", inline = True)


#--------------------------------


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_rapier = discord.Embed(title="Info Stocco", color=discord.Color.green(), inline=True)
embed_rapier.set_thumbnail(url="attachment://spear.jpg")
#embedrapierembed_rapierr.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_rapier.add_field(name = 'Scaling', value= f"> destrezza: `0.9` \n > intelligenza: `0.65`", inline = False)
embed_rapier.add_field(name = 'Tipo di danno', value = "> Affondo", inline = False)


#--------------------------------


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_hatchet = discord.Embed(title="Info Accette", color=discord.Color.green(), inline=True)
embed_hatchet.set_thumbnail(url="attachment://spear.jpg")
#embedhatchetr.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_hatchet.add_field(name = 'Scaling', value= f"> destrezza: `0.65` \n > forza: `0.9`", inline = False)
embed_hatchet.add_field(name = 'Tipo di danno', value = "> Taglio", inline = False)


#--------------------------------


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_spear = discord.Embed(title="Info lancia", color=discord.Color.green(), inline=True)
embed_spear.set_thumbnail(url="attachment://spear.jpg")
#embed_spear.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_spear.add_field(name = 'Scaling', value= f"> destrezza: `0.9` \n > forza: `0.65`", inline = False)
embed_spear.add_field(name = 'Tipo di danno', value = "> Affondo", inline = False)


#--------------------------------


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_great_axe = discord.Embed(title="Info Ascia bipenne", color=discord.Color.green(), inline=True)
embed_great_axe.set_thumbnail(url="attachment://spear.jpg")
#embedgreat_axer.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_great_axe.add_field(name = 'Scaling', value= f"> forza: `1.00`", inline = False)
embed_great_axe.add_field(name = 'Tipo di danno', value = "> Taglio", inline = False)


#--------------------------------


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_war_hammer = discord.Embed(title="Info Martello da guerra", color=discord.Color.green(), inline=True)
embed_war_hammer.set_thumbnail(url="attachment://spear.jpg")
#embedwar_hammerr.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_war_hammer.add_field(name = 'Scaling', value= f"> forza: `1.00`", inline = False)
embed_war_hammer.add_field(name = 'Tipo di danno', value = "> Colpo", inline = False)


#--------------------------------


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_bow = discord.Embed(title="Info Arco", color=discord.Color.green(), inline=True)
embed_bow.set_thumbnail(url="attachment://spear.jpg")
#embedbowr.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_bow.add_field(name = 'Scaling', value= f"> destrezza: `1.00`", inline = False)
embed_bow.add_field(name = 'Tipo di danno', value = "> Affondo", inline = False)


#--------------------------------


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_musket = discord.Embed(title="Info Moschetto", color=discord.Color.green(), inline=True)
embed_musket.set_thumbnail(url="attachment://spear.jpg")
#embedmusketr.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_musket.add_field(name = 'Scaling', value= f"> destrezza: `0.9` \n > intelligenza: `0.65`", inline = False)
embed_musket.add_field(name = 'Tipo di danno', value = "> Affondo", inline = False)


#--------------------------------


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_fire_staff = discord.Embed(title="Info Staffa del fuoco", color=discord.Color.green(), inline=True)
embed_fire_staff.set_thumbnail(url="attachment://spear.jpg")
#embedfire_staffr.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_fire_staff.add_field(name = 'Scaling', value= f"> intelligenza: `1.00`", inline = False)
embed_fire_staff.add_field(name = 'Tipo di danno', value = "> Elementale", inline = False)


#--------------------------------


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_life_staff = discord.Embed(title="Info Staffa della vita", color=discord.Color.green(), inline=True)
embed_life_staff.set_thumbnail(url="attachment://spear.jpg")
#embedlife_staffr.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_life_staff.add_field(name = 'Scaling', value= f"> focus: `1.00`", inline = False)
embed_life_staff.add_field(name = 'Tipo di danno', value = "> Elementale", inline = False)


#--------------------------------


#file = discord.File(r"C:\Users\mirko\Desktop\DiscordBot\imgs\spear.jpg", filename="Spear.jpg")
embed_ice_gauntlet = discord.Embed(title="Info guanto del ghiaccio", color=discord.Color.green(), inline=True)
embed_ice_gauntlet.set_thumbnail(url="attachment://spear.jpg")
#embedice_gauntletr.set_author(name="IMMORTAL BOT\n", icon_url=file)
embed_ice_gauntlet.add_field(name = 'Scaling', value= f"> intelligenza: `1.00`", inline = False)
embed_ice_gauntlet.add_field(name = 'Tipo di danno', value = "> Elementale", inline = False)
