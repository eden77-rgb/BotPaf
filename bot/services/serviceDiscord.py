import discord
from discord.ext import commands
from services.serviceYoutube import serviceYoutube

class serviceDiscord:
    def __init__(self, token):
        self._token = token

        _intents = discord.Intents.default()
        _intents.message_content = True

        self._bot = commands.Bot(command_prefix="!", intents=_intents)
        self._youtube = serviceYoutube()    

        self.setup_events()
        self.setup_commands()

    def setup_events(self):
        @self._bot.event
        async def on_ready():
            print(f"Connecté en tant que {self._bot.user.name}")

    def setup_commands(self):
        @self._bot.command()
        async def aide(ctx):
            await ctx.send("!play [nom musique]: pour obtenir le lien youtube")

        @self._bot.command()
        async def play(ctx, *, search):
            result = self._youtube.search(search)
            if result:
                await ctx.send(f"Voici ce que j'ai trouvé pour **{search}** :\n{result['title']}\n{result['url']}")
            else:
                await ctx.send("Désolé, je n'ai rien trouvé.")

    def run(self):
        self._bot.run(self._token)
