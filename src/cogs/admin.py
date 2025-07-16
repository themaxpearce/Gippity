import discord
from discord.ext import commands
from discord import app_commands

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="instruction", description="Manage custom instructions")
    async def manage_instruction(self, interaction: discord.Interaction, scope: str, option: str, instruction: str):
        await interaction.response.send_message(f"You requested to {option} at scope {scope}: {instruction}")
