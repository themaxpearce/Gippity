import discord
from gippity import Gippity
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("bot_token")
ai_key = os.getenv("ai_key")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True

client = Gippity(command_prefix="g!", intents=intents)

@client.event
async def on_ready():
    print("Bot Ready")

async def main():

    async with client:
        await client.start(bot_token)

asyncio.run(main())
