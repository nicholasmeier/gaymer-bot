# constants.py
# private ids
TOKEN = "PUTYOURBOTTOKENINHERE"
### gamer server
HORNYJAIL_ID = -1
GENERAL_ID = -1
### devtest server
DEV_TEST_ID = -1
### Misc server details
ADMINROLES = ["admin", "owner"]

# filestorenames
TIMERH = "textstores/hornytimer.txt"
TIMERT = "textstores/toddtimer.txt"

# Todd
TODDHOWARD = ["todd", "todd howard", "howard", "godd howard", "hodd toward", "sodd howard", "skyrim", "god howard", "toddd", "talos", "thanks todd", "thanks tod"]

# Game Maps
GAMES_HORROR = [["REPO", 3241660], ["The Outlast Trials", 1304930], ["Lethal Company", 1966720], ["Happy's Humble Burger Cult", 3453910], ["The Mound", 2569760], ["Undermire", 3366370], ["Machine Party", 4108000], ["Shift at Midnight", 3722330], ["Cursed Companions", 3265230], ["Pit of Goblin", 3253530], ["Flyknight", 3108510] ]
GAMES_SHOOT = [["GTFO", 493520], ["Risk of Rain 2", 632360], ["Helldivers 2", 553850], ["Vermintide 2", 552500], ["Left 4 Dead 2", 550], ["Grain Rot", 4450620], ["How to Fish", 4001890], ["Tears of Metal", 1913120], ["Friends vs Friends", 1785150], ["Splitgate", 677620], ["Deep Rock Galactic", 548430], ["Barony", 371970], ["Borderlands 2", 49520], ["Gunfire Reborn", 1217060]]
GAMES_CHILL = [["SHORE", 4280880], ["Castle Crashers", 204360], ["Duck Game", 312530], ["slay the spire 2", 2868840], ["pico park", 1509960], ["Torchlight II", 200710], ["Monster Prom", 743450], ["Trine", 35700], ["The Long Drive", 1017180], ["Jump Space", 1757300], ["SpiderHeck", 1329500], ["Human Fall flat", 477160], ["BOMBANANA", 4656000], ["The One Fish", 4883580], ["Cat Mail Co", 4380490], ["Roadside Research", 3643170], ["Embr", 1062830], ["Plate up", 1599600], ["Burglin Gnomes", 3844970], ["Super Battle Golf", 4069520], ["Mechachameleon", 4704690], ["Dale and Dawson", 2920570], ["Goblin Cleanup", 2748340], ["Golf with Friends", 431240], ]
GAMES_CRAFT = [["Cloudheim", 2070270], ["Roco Kingdom", 4821880], ["Windrose", 3041230], ["valheim", 892970], ["terraria", 105600], ["core keeper", 1621690], ["Grounded", 962130], ["Trail and Error", 4322960], ["Sons of the forest", 1326470], ["Don't starve together", 322330], ["Abiotic Factor", 427410], ["Palworld", 1623730]]
STEAMTEMPLATE = "https://store.steampowered.com/app/"

FULL_COMMAND_LIST = "!about - Shows the about page in discord - replaced !help\n" \
                    "!commandsall - prints this page in your DMs\n" \
                    "!bonk <@user> - Use to bonk a specific user in the server. Send with no args to send a bonk with no target. Resets the horny-jail counter\n" \
                    "!daycount - Check the count of \n" \
                    "!honey - Use to give the bot honey :)\n" \
                    "!game <chill|horror|craft|shooter> - Use an arg to pick a game from a list of preselected games. Or just use without args to send a random game from all genres\n" \
                    "!role <rolename> - give yourself a role in the server"