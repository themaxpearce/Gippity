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
    async def manage_instruction(self, interaction: discord.Interaction, scope: str, option: str, instruction: str = ""):

        if option.lower() not in ["add", "view", "remove"]:
            return
   
        obj = None
        if scope == "guild":
            obj = interaction.guild
        elif scope == "channel":
            obj = interaction.channel


        if option == "add":

            if len(instruction) < 0:
                await interaction.response.send_message("No instruction provided!")
                return
            

            await self.bot.addConfigToObject(obj, "instruction", instruction)
        
            await interaction.response.send_message(f"Successfully added instruction to {obj.name}") 
        
        elif option == "view":
            
            config = await self.bot.getObjectConfig(obj)
            print(config)
            
            embed = discord.Embed(
            title="Config",
            description=f"Current config for {obj.name}"
            )
            
            for key in config:
                embed.add_field(name=key, value=config[key])

            await interaction.response.send_message(embed=embed)

            #print("Someone wants to view instructions")

        elif option == "remove":
            print("Someone wants to remove instructions")

        else:
            print("Uh oh")




        
