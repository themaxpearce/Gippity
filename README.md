# Gippity
A simple Discord bot that connects to an AI interface.

# Setting up the bot
The bot requires certain environment variables to be set
These can be done either within the environment (useful for Heroku and other hosts).
Alternatively, create a .env file in the directory from which you run the program.

The following variables are needed:
bot_token - The Discord bot token
ai_key - The OpenAI API Key

# Using the bot
Running the bot is as simple as executing the main.py file.
By default, users can mention the bot in a message and it'll respond to that message within the context of the channel.
