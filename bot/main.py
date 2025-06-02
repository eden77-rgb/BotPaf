import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import yt_dlp

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="?", intents=intents)
token = os.getenv("DISCORD_BOT_TOKEN")

ytdl_format_options = {
    "format": "bestaudio/best",
    "quiet": True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'no_warnings': True,
    'default_search': 'ytsearch'
}

ytdl = yt_dlp.YoutubeDL(ytdl_format_options)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user.name}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def play(ctx, *, search):
    try:
        info = ytdl.extract_info(f"ytsearch:{search}", download=False)["entries"][0]
        url = info["webpage_url"]
        titre = info['title']
        
        await ctx.send(f"Voici ce que j'ai trouvé pour **{search}** :\n{titre}\n{url}")

    except Exception as e:
        await ctx.send("Désolé, je n'ai rien trouvé.")
        print(f"Erreur play : {e}")

bot.run(token)
