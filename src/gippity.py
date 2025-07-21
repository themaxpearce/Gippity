import discord
from discord.ext import commands
import datetime

class Gippity(commands.Bot):

    # Override commands.Bot setup hook to allow for extra data to load before setup
    async def setup_hook(self):
        print("Hello")

    ###################
    # SETUP FUNCTIONS #
    ###################
    
    # Used to load guild and channel config
    async def load_configs(self):
        print("Loading guild and channel configs to memory")
        
        # Store configs into memory
        self._guild_config = {}

    async def load_config_for_guild(self, guild: discord.Guild):
       
        # guild_config[guildid] will hold all config data relevant to guild
        # "channels" and "global" distinguish between individual channel config and guild-wide config
        self._guild_config[guild.id] = {
                ["channels"]:{},
                ["global"]:{},
                }

    async def addConfigToObject(self, discordObject, option, config):
        if type(discordObject) == discord.Guild:
            print("Adding config to guild")
        elif type(discordObject) == discord.TextChannel:
            print("Adding config to text channel")
        else:
            print("Whoops! Can't config here :/")
        return

    async def getObjectConfig(self, discordObject):
        
        if type(discordObject) == discord.Guild:
            if discordObject.id in self._guild_config:
                return self._guild_config[guild.id]["global"]

        elif type(discordObject) == discord.TextChannel:
            # If channel guild is configured
            if discordObject.guild.id in self._guild_config:
                # If channel is configured within said guild
                if discordObject.id in self._guild_config[discordObject.guild.id]["channels"]:
                    return self._guild_config[discordObject.guild.id]["channels"][discordObject.id]

        return None 

    async def getObjectConfigOption(self, discordObject, option):
        
        objectConfig = self.getObjectConfig(discordObject)
        if objectConfig is not None:
            if option in objectConfig:
                return objectConfig[option]
        
        return None


    ######################
    # CORE FUNCTIONALITY #
    ######################

    # Used to get instructions from added context
    # Modify to customise instructions GLOBALLY
    # Some options can be passed to msg_ctx to customise certain parameters per guild
    async def genInstructions(self, msg_ctx: dict = {}):
        instructions = "You are a British human on the platform Discord. Your name is Gippity. "
        instructions += "When speaking English, make sure to always use British English unless explicitly asked otherwise. "
        instructions += "You can tag a user by using <@USERID> where USERID is the number associated with their account. "
        
        if "previous_messages" in msg_ctx:
            instructions += f"Provided is a list of previous messages for added context: {msg_ctx['previous_messages']}. " 
        
        if "author" in msg_ctx:
            instructions += f"The current message was sent by User {msg_ctx['author'].id} (username: {msg_ctx['author'].name}). "

        if "datetime" in msg_ctx:
            time, date = self.formatTime(msg_ctx["datetime"])
            instructions += f"The current message was sent at {time} on {date}. "

        return instructions


    # Handles actually generating instructions from message
    # Use this instead of genInstructions if you don't need raw control over every argument
    async def genInstructionsFromMessage(self, message: discord.Message, msg_ctx: dict = {}):

        print("Generating Instruction Set")

        if "previous_messages" not in msg_ctx:
            print("Previous Messages not provided, generating own")
            previous_messages = [msg async for msg in message.channel.history(limit=51)][::-1][:-1]

            msg_ctx["previous_messages"] = list(map(self.formatMessage, previous_messages))

        msg_ctx["author"] = message.author
        msg_ctx["datetime"] = message.created_at

        instructions = await self.genInstructions(msg_ctx)

        return instructions


    ####################
    # HELPER FUNCTIONS #
    ####################

    # Format message time to standard format
    def formatTime(self, sent: datetime.datetime):

        time = f"{sent.hour}:{sent.minute} UTC"
        date = f"{sent.day}-{sent.month}-{sent.year}"
    
        return time, date

    # Format message for message list
    def formatMessage(self, message: discord.Message):

        _sent = message.created_at
        time, date = self.formatTime(_sent)

        user = ""
        if message.author == self.user:
            user = "you"
        else:
            user = f"User {message.author.id} (username: {message.author.name})"

        msgString = f"At {time} on {date}, {user} said: {message.content}"

        return msgString
