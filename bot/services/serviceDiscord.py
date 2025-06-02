import discord
from discord.ext import commands
from services.serviceYoutube import serviceYoutube

class serviceDiscord:
    def __init__(self, token):
        self.token = token

        intents = discord.Intents.default()
        intents.message_content = True

        self.bot = commands.Bot(command_prefix="?", intents=intents)
        self.youtube = serviceYoutube()

        self.setup_events()
        self.setup_commands()

    def setup_events(self):
        @self.bot.event
        async def on_ready():
            print(f"Connecté en tant que {self.bot.user.name}")

    def setup_commands(self):
        @self.bot.command()
        async def ping(ctx):
            await ctx.send("Pong!")

        @self.bot.command()
        async def play(ctx, *, search):
            result = self.youtube.search(search)
            if result:
                await ctx.send(f"Voici ce que j'ai trouvé pour **{search}** :\n{result['title']}\n{result['url']}")
            else:
                await ctx.send("Désolé, je n'ai rien trouvé.")

    def run(self):
        self.bot.run(self.token)
