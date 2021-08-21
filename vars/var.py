import discord
import dislash
from wepembed import *
from dislash import *

vocal_number = 0
ruoli2 = ["Triumviri", "[I]Legato", "[II]Tribuno", "[III]Prefetto", "[IV]Centurione", "[V]Decano", "[VI]Istruttore", "[VII]Veterano", "[VIII]Legionario", "[XI]Recluta"]
ruoli = ["[I]Legato", "[II]Tribuno", "[III]Prefetto", "[IV]Centurione", "[V]Decano", "[VI]Istruttore", "[VII]Veterano", "[VIII]Legionario", "[X]Ausiliario", "[XI]Recluta"]
checkgradi = ["[I","[II","[III","[IV","[V","[VI","[VII","[VIII","[X","[XI"]
gradi = ["[I]","[II]","[III]","[IV]","[V]","[VI]","[VII]","[VIII]","[X]","[XI]"]
img = url="https://t3.ftcdn.net/jpg/01/22/80/68/240_F_122806803_hz1FsXp4I0sAruQAwzv8Lw894Oyw5XXc.jpg"
ruoliembed = f"0 - Triumviri \n 1 - [I]Legato \n 2 - [II]Tribuno \n 3 - [III]Prefetto \n 4 - [IV]Centurione \n 5 - [V]Decano \n 6 - [VI]Istruttore \n 7 - [VII]Veterano \n 8 - [VIII]Legionario \n 9 - [XI]Recluta"
emoji_numbers = ["0️⃣","1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
#], "\n", "1 - [I]Legato", "\n", "2 - [II]Tribuno", "\n", "3 - [III]Prefetto", "\n", "4 - [IV]Centurione", "\n", "5 - [V]Decano", "\n", "6 - [VI]Istruttore", "\n", "7 - [VII]Veterano", "\n", "8 - [VIII]Legionario", "\n", " 9 - [X]Ausiliario", "\n", "10 - [XI]Recluta"]

admin_row = ActionRow(
    Button(
        style=ButtonStyle.red,
        label="Admin commands",
        custom_id="admin"
    ),
    Button(
        style=ButtonStyle.red,
        label="User commands",
        custom_id="user"
    )
)

user_row = ActionRow(
    Button(
        style=ButtonStyle.red,
        label="Admin commands",
        custom_id="admin",
        disabled=True
    ),
    Button(
        style=ButtonStyle.red,
        label="User commands",
        custom_id="user"
    )
)


name = ".vrole"
description = "filter member(s) by role"
example = ".bot"


embed_user = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
embed_user.set_thumbnail(url=img)
embed_user.set_author(name="IMMORTAL BOT\n", icon_url=img)
embed_user.add_field(name = 'name', value= name, inline = True)
embed_user.add_field(name = 'description', value = description, inline = True)
embed_user.add_field(name = 'example', value = example, inline = True)






#----------------------------------------
info_row_1 = ActionRow(
    Button(
        style=ButtonStyle.blurple,
        emoji="🔼",
        custom_id="up",
        disabled=False
    ),

    Button(
        style=ButtonStyle.green,
        emoji="✅",
        custom_id="enter",
    ),
)

info_row_2 = ActionRow(
    Button(
        style=ButtonStyle.blurple,
        emoji="🔽",
        custom_id="down",
    ),
    Button(
        style=ButtonStyle.red,
        emoji="✖",
        custom_id="back",
    )
)
#-------------------------------------------
disabled_info_row_1 = ActionRow(
    Button(
        style=ButtonStyle.blurple,
        emoji="🔼",
        custom_id="up",
        disabled=True
    ),

    Button(
        style=ButtonStyle.green,
        emoji="✅",
        custom_id="enter",
        disabled=True
    ),
)

disabled_info_row_2 = ActionRow(
    Button(
        style=ButtonStyle.blurple,
        emoji="🔽",
        custom_id="down",
        disabled=True
    ),
    Button(
        style=ButtonStyle.red,
        emoji="✖",
        custom_id="back",
    )
)
#----------------------------------------

main_info_page = [
    "Comandi per admin\n",
    "Comandi generali\n",
]

#command info
admin_command_page = [
    ".reset",
    ".rank"
]
user_command_page = [
    ".vrole",
    ".f"
]

page_1 = [
    "main_info_page",
    "admin_command_page",
    "user_command_page",
]
page_2 = [
    "admin_command_page",
    ".reset",
    ".rank"
]
page_3 = [
    "user_command_page",
    ".vrole",
    ".f"
]
current_line = 0
current_page = 0
embed_main_info = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
embed_main_info.set_author(name="IMMORTAL BOT\n", icon_url=img)
embed_main_info.add_field(name = '\u200b', value= "".join(main_info_page))


embed_weapon_info = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
embed_weapon_info.set_author(name="IMMORTAL BOT\n", icon_url=img)
embed_weapon_info.add_field(name = '\u200b', value= "".join(weapon_page))
current_line = 0


components=[
    SelectMenu(
        custom_id="test",
        placeholder="Choose up to 2 options",
        max_values=2,
        options=[
            SelectOption("Option 1", "value 1"),
            SelectOption("Option 2", "value 2"),
            SelectOption("Option 3", "value 3")
        ]
    )
]