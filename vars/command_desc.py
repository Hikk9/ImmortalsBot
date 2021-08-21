import discord
from vars.var import *
from vars.wepembed import *

reset_value = f"Con questo comando comando si resettano i nickname di tutti i presenti nel server, riportandoli al loro nome usato dalla account \n esempio: \n nome account: \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b nickname nel server:\n> Hik#9778 \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b \u200b Izalith\n dopo il comando `.reset` il nick sul server diventerà: \n> Hik"
embed_reset_info = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
embed_reset_info.set_author(name="IMMORTAL BOT\n", icon_url=img)
embed_reset_info.add_field(name = 'Comando reset', value= reset_value)



rank_value = f"Con questo comando viene aggiornato il prefisso nel nickname basandosi sul ruolo corrente\n esempio:\nnickname: `[X]Hik`, ruolo:`[VII] Veterano` \n dopo il comando il nickname diventerà \n > [VII] Hik "
embed_rank_info = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
embed_rank_info.set_author(name="IMMORTAL BOT\n", icon_url=img)
embed_rank_info.add_field(name = 'Comando reset', value= rank_value)



f_value = f"Con questo comando si possono avere info sull'arma richiesta\n esempio:\n> `.f lancia`\n \u200b \nPer ulteriori informazioni scrivere\n> `.f info`"
embed_f_info = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
embed_f_info.set_author(name="IMMORTAL BOT\n", icon_url=img)
embed_f_info.add_field(name = 'Comando reset', value= f_value)



vrole_value = f"Con questo comando si può vedere la lista membri di un determinato ruolo\n esempio:\n> `.vrole`"
embed_vrole_info = discord.Embed(title="Commands Information", color=discord.Color.green(), inline=True)
embed_vrole_info.set_author(name="IMMORTAL BOT\n", icon_url=img)
embed_vrole_info.add_field(name = 'Comando reset', value= rank_value)