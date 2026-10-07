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

def get_role(guild, role_name):
    if guild == "DMMESSAGE":
        return -1
    for role in guild.roles:
        if role.name.lower() == role_name.lower():
            return role
    return -1

def get_game(genre = None):
    if genre == "chill":
        g_c = random.randrange(0, len(constants.GAMES_CHILL))
        gamechoice = constants.GAMES_CHILL[g_c]
        return gamechoice
    elif genre == "shooter":
        g_c = random.randrange(0, len(constants.GAMES_SHOOT))
        gamechoice = constants.GAMES_SHOOT[g_c]
        return gamechoice
    elif genre == "horror":
        g_c = random.randrange(0, len(constants.GAMES_HORROR))
        gamechoice = constants.GAMES_HORROR[g_c]
        return gamechoice
    elif genre == "craft":
        g_c = random.randrange(0, len(constants.GAMES_CRAFT))
        gamechoice = constants.GAMES_CRAFT[g_c]
        return gamechoice
    else:
        gamelist = constants.GAMES_CHILL + constants.GAMES_CRAFT + constants.GAMES_HORROR + constants.GAMES_SHOOT
        g_c = random.randrange(0, len(gamelist))
        gamechoice = gamelist[g_c]
        return gamechoice

    
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

# do a daily count at 5pm et
daily = datetime.time(hour=21, minute=0, second=0)

@tasks.loop(time=daily)
async def counter():
    channel = client.get_channel(constants.GENERAL_ID)
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
    if message.guild:
        guild = client.get_guild(message.guild.id)
    else:
        guild = "DMMESSAGE"
    text_channel = client.get_channel(constants.HORNYJAIL_ID).mention

    # help
    if message.content.startswith('!about'):
        await message.channel.send("Greetings, I am the big gay bear (specifically I am a bisexual sun bear).\nUse !daycount to see how long since the last incident.\nUse !honey to give me a treat :)\nUse !commandsall to get a full list of commands in your DMs")

    # all commands
    if message.content.startswith('!commandsall'):
        a_chan = await message.author.create_dm()
        await a_chan.send(constants.FULL_COMMAND_LIST)

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

    # get a random game
    if message.content.startswith('!game'):
        suggestgame_args = message.content.split(" ")
        if len(suggestgame_args) < 2:
            game_details = get_game()
        else:
            game_details = get_game(suggestgame_args[1])
        msg = "Try this game: " + game_details[0] + "\n" + constants.STEAMTEMPLATE + str(game_details[1])
        await message.channel.send(msg)

    # give role
    if message.content.startswith('!giverole'):
        giverole_args = message.content.split(" ")
        if len(giverole_args) < 2:
            await message.channel.send("Sorry, you need to pick a role to give yourself.")
        else:
            rolename = giverole_args[1]
            if len(giverole_args) > 2:
                for i in range(2, len(giverole_args)):
                    rolename = rolename + " " + giverole_args[i]
            member = message.author
            role = get_role(guild, rolename)
            if giverole_args[1].lower() in constants.ADMINROLES:
                await message.channel.send("Nice try bub! You get the tongue now >:P", file=discord.File("imgs/sunbeartongue.jpg"))
            elif role != -1:
                await member.add_roles(role)
                await message.channel.send("Nice! You've been made into a {0}".format(role.name))
            else:
                await message.channel.send("Sorry, I can't find that role.", file=discord.File("imgs/sadsunbear.jpg"))

    # todd
    if any(substring in message.content.lower() for substring in constants.TODDHOWARD):
        ttimer_msg = 'It has now been 0 days since the forbidden sequence was mentioned. It was previously {0} days'.format(get_count(constants.TIMERT))
        update_count(constants.TIMERT, 0)
        await message.channel.send(ttimer_msg)

client.run(constants.TOKEN)