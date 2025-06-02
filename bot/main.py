import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="?", intents=intents)
token = os.getenv("DISCORD_BOT_TOKEN")

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user.name}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def baiseur(ctx):
    await ctx.send("Je suis Loic Arthur NKWINDJA BIEDA")

bot.run(token)
