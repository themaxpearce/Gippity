import discord
from discord.ext import commands
from discord import app_commands

# Admin cog handles all commands relevant to guild admins
# Cog relies on some gippity-specific functions. Will not be a drop in replacement for cogs in other bots.


class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="instruction", description="Manage custom instructions")
    @app_commands.describe(
            scope="Guild-wide or channel-specific instruction",
            option="Add, view or remove instructions",
            instruction="The new instruction, or the instruction to remove",
    )
    async def manage_instruction(self, interaction: discord.Interaction, scope: str, option: str, instruction: str):

        if option == "add":
            print("Someone wants to add instructions")
        
        elif option == "view":
            print("Someone wants to view instructions")

        elif option == "remove":
            print("Someone wants to remove instructions")

        else:
            print("Uh oh")




        await interaction.response.send_message(f"You requested to {option} at scope {scope}: {instruction}")
