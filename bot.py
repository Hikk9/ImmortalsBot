import sys

from discord.channel import VoiceChannel
sys.path.append('C:/Users/mirko/Desktop/DiscordBot/cogs/' )
sys.path.append('C:/Users/mirko/Desktop/DiscordBot/vars/' )
import discord
from discord.ext import commands
import builtins
from discord.ext.commands.errors import CommandNotFound
from dislash import *
from vars import *

#----------------------------------------------------------------------------

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
builtins.bot = client
SlashClient(client)
client.remove_command('help')


#----------------------------------------------------------------------------



'''@client.event #.error do not exist, need something else
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        print("yep")
        return
    raise error'''

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_voice_state_update(member, before, after):
    if str(after.channel) == 'crea canale pvp':
        if str(after) != str(before):
            new_channel = await after.channel.clone(name=f'canale vocale di {member.name}')
            #new_channel = client.get_channel(f'canale vocale #{vocal_number}')
            print(new_channel)
            await member.move_to(new_channel)
        print(f"len: {len(after.channel.members)}")
    print(before)
    print(after)
    print("---------------------")
    if str(before.channel) == f'canale vocale di {member.name}':
        if len(before.channel.members) == 0:
            print(f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa: {before}")
            await before.channel.delete()

'''    if len(after.channel.members) == 0:
        print(f"len2: {len(after.channel.members)}")
        '''



client.load_extension('cogs.chnick')
client.load_extension('cogs.rank')
client.load_extension('cogs.reset')
client.load_extension('cogs.viewrole')
client.load_extension('cogs.fast_info')
client.load_extension('cogs.help')
#client.run('process.env.token')
client.run('ODY1OTE0NjUzOTg4NDg3MTY5.YPK73Q.3yrTnzDHyEeJu7jXLBCZFUu5lEU')
