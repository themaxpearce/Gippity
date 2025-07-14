import discord
from gippity import Gippity
import asyncio
import os
from dotenv import load_dotenv
from interface import Responder

load_dotenv()

bot_token = os.getenv("bot_token")
ai_key = os.getenv("ai_key")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True
#intents.mentions = True

client = Gippity(command_prefix="g!", intents=intents)
responder = Responder(ai_key)

@client.event
async def on_ready():
    print("Bot Ready")

@client.tree.command(name="sync", description="Owner only command")
async def sync(interaction: discord.Interaction):
    if interaction.user.id == 274620118795812864:
        print("Requested tree sync")
        await client.tree.sync()

        print("Tree has synced")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user not in message.mentions:
        return
    
    instructions = await client.genInstructionsFromMessage(message)
    response = responder.generate_response(message.content, instructions) 

    # Send response to discord
    # TODO: Add controls for longer messages
    await message.channel.send(response)

async def main():

    async with client:
        await client.start(bot_token)

asyncio.run(main())
