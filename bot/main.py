import os
from dotenv import load_dotenv

from services.serviceDiscord import serviceDiscord

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if __name__ == "__main__":
    bot = serviceDiscord(TOKEN)
    bot.run()
