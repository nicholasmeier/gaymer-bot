import discord
import logging
import random

import constants


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

debug = False
## 
#
# Helper Funcs
#
##

"""
def get_random_game(genre):
    gamesfile = open("games.txt", "r")
    game_lists = gamesfile.read().splitlines()
    if genre == "" | genre == "all":
        for game_list in game_lists:
    elif genre == "horror":
    elif genre == "cozy":
    elif genre == "shooter":
"""     
    

## 
#   
# Discord funcs  
#  
##
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    horny_jail = client.get_channel('')

    # no self-respond
    if message.author == client.user:
        return
    #get guild
    guild = client.get_guild(message.guild.id)
    text_channel = client.get_channel(constants.HORNYJAIL_ID).mention

    # bonk horny jail
    if message.content.startswith('!bonk'):
        pickplayer_args = message.content.split(" ")
        if not message.mentions:
            await message.channel.send(file=discord.File('imgs/bonk.jpg'))
        else:
            member = message.mentions[0]
            await message.channel.send(file=discord.File('imgs/bonk.jpg'))
            msg = '{0} BONK! Go to {1}'.format(member.mention, text_channel)
            await message.channel.send(msg)

client.run(constants.TOKEN)