# import important packages we need to make the code work
import discord
from discord import app_commands
import logging
import asyncio

# add a file to store logs in (IMPROTANAT FOR FIXING BUGS/LOOPHOLES)
logger = logging.getLogger('discord') # does something (I think it logs from discord)
logger.setLevel(logging.DEBUG) # makes debug data avalible
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') # acctually makes the file
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')) # gives us date and time of the log (like maybe an error or amth idk)
logger.addHandler(handler) # makes the logger use the logger to log the data (sry I can't explain it well)

# give the bot permisions
intents = discord.Intents(messages=True, guilds=True)

# init the bot with the declared permissions
bot = discord.Client(intents=intents)
# give the bot a tree for commands
tree = app_commands.CommandTree(bot)
print("grow grow grow")

@bot.event
# when sturtup is started do stratup things
async def on_ready(self):
    # define very important variables
    global chat_reviver_id # naming the revive_chat role id variable and making it
    chat_reviver_id = 1133066338479378565 # giveng the variable the id

    # log a startup
    print(f'logged in as {self.user} (ID: {self.user.id})')
    try: # attempt something
        synced = await bot.tree.sync() # attempt to sync commands from the bot.tree
        print(f'synced {len(synced)} commands') # print the number of synced commands on sucses (I can't spell)
    except Exception as e: # catch an exception
        print(e) # print the exception

@bot.event
# when a message is sent execute on_messsage
async def on_message(message):
    if not message.author.bot: # if the message is from a bot do nothing
        return # does nothing :(

    global timer_task # make a timer variable
    timer_task = asyncio.create_task(asyncio.sleep(300)) # set the timer

# make a command, describe it, and make it server exclusive
@tree.command(name = 'chat-reviver', description = 'PING EVERYONE WITH THE CHAT REVIVER ROLE🔥🔥🔥', guild = discord.Object(id = 1132738865652826263))
@app_commands.describe(message = "Wanna say anything to chat?.") # add arguments
async def chat_message(interaction: discord.Interaction, message: str): # add arguments again cuz that's the syntax 🔥🔥🔥
    if "Mods" in interaction.message.author.roles and not timer_task.done(): # if
        await interaction.channel.send(f" <&{chat_reviver_id}> \n{interaction.user.mention}: would like to revive chat with an urgent message! \n{message}")  # revive chat urgently
    if timer_task.done() : # if the cooldown has finished proceed with the next block of code
        await interaction.channel.send(f" <&{chat_reviver_id}> \n{interaction.user.mention}: would like to revive chat with a lovely message! \n{message}") # revive chat
    if not timer_task.done(): # otherwise
        await interaction.channel.send(f"the timer hasn't ended please wait 5 minutes", ephemeral = True) # make them wait
    if "Prisoner" in interaction.message.author.roles:
        await interaction.channel.send(f" # ```BUT NO ONE CAME...``` ", ephemeral = True)
