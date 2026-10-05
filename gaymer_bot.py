import datetime
import discord
from discord.ext import tasks
import logging
import random

import constants


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

debug = True
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
    
def get_count(filename):
    countfile = open(filename, "r")
    count = int(countfile.read())
    countfile.close()
    return count

def update_count(filename, count):
    countfile = open(filename, "w")
    countfile.write(str(count))
    countfile.close()

## 
#   
# Discord funcs  
#  
##
daily = datetime.time(hour=21, minute=37, second=0)

@tasks.loop(time=daily)
async def counter():
    channel = client.get_channel(constants.DEV_TEST_ID)
    # update counters
    msg_counter = 'Greetings! Here is the daily counter update:\n'
    ## Bonk counter
    tmpcnt = get_count(constants.TIMERH)
    count = tmpcnt+1
    update_count(constants.TIMERH, count)
    msg_counter_h = 'It has now been {0} days since the last horny incident.\n'.format(count)

    ## Todd Counter 
    tmpcnt = get_count(constants.TIMERT)
    count = tmpcnt+1
    update_count(constants.TIMERT, count)
    msg_counter_t = 'It has now been {0} days since the forbidden sequence was last mentioned.'.format(count)
    await channel.send(msg_counter + msg_counter_h + msg_counter_t)
    if debug:
        print("DEBUG: SENT COUNTER MESSAGES")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    if not counter.is_running():
        counter.start()
        print("counter task started")

@client.event
async def on_message(message):
    horny_jail = client.get_channel('')

    # no self-respond
    if message.author == client.user:
        return
    #get guild
    guild = client.get_guild(message.guild.id)
    text_channel = client.get_channel(constants.DEV_TEST_ID).mention

    # help
    if message.content.startswith('!help'):
        await message.channel.send("Greetings, I am the big gay bear (specifically I am a bisexual sun bear).\nUse !bonk <@user> to send someone to horny jail.\nUse !daycount to see how long since the last incident.\nUse !honey to give me a treat :)")

    # bonk horny jail
    if message.content.startswith('!bonk'):
        pickplayer_args = message.content.split(" ")
        timer_msg = 'It has now been 0 days since the last bonk. It was previously {0} days'.format(get_count(constants.TIMERH))
        update_count(constants.TIMERH, 0)
        if not message.mentions:
            await message.channel.send(timer_msg, file=discord.File('imgs/bonk.jpg'))
        else:
            member = message.mentions[0]
            msg = '{0} BONK! Go to {1}\n'.format(member.mention, text_channel)
            await message.channel.send(msg + timer_msg, file=discord.File('imgs/bonk.jpg'))

    # get bonk day counter
    if message.content.startswith('!daycount'):
        h_count = get_count(constants.TIMERH)
        t_count = get_count(constants.TIMERT)
        dc_msg = 'It has been {0} days since the last horny incident.\n'.format(h_count)
        todd_msg = 'It has been {0} days since [REDACTED] was mentioned'.format(t_count)
        await message.channel.send(dc_msg + todd_msg)

    # give bear honey
    if message.content.startswith('!honey'):
        await message.channel.send("Thank you friend! Your honey is much appreciated", file=discord.File('imgs/sunbearhoney.jpg'))

    # todd
    if any(substring in message.content.lower() for substring in constants.TODDHOWARD):
        ttimer_msg = 'It has now been 0 days since the forbidden sequence was mentioned. It was previously {0} days'.format(get_count(constants.TIMERT))
        update_count(constants.TIMERT, 0)
        await message.channel.send(ttimer_msg)

client.run(constants.TOKEN)