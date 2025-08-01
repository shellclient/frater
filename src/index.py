import src.Cogs.Music as Music, src.Cogs.Fun as Fun, src.Cogs.Utils as Utils
import discord, os, pomice
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=os.getenv('PREFIX'), intents=intents)

cogs = [Fun, Utils]

bot.remove_command('help')  # remove default help command

@bot.event
async def on_ready():
    # setting up commands
    for i in range(len(cogs)):
        await cogs[i].setup(bot)

    #setting up music cog
    await Music.setup(bot)
    music = Music.Music(bot)
    await music.start_nodes()

    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f" {bot.command_prefix}help"))
    
    print(f"{bot.user} is Ready!")
    

bot.run(os.getenv('TOKEN'))