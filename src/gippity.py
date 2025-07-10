import discord
from discord.ext import commands

class Gippity(commands.Bot):

    def getInstructions(self, msg_ctx: dict = {}):
        instructions = "You are a British human on the platform Discord. Your name is Gippity. "

        return instructions


    
