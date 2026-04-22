import discord
from discord.ext import commands
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Load configuration
from config import TOKEN, PREFIX

# Initialize bot
bot = commands.Bot(command_prefix=PREFIX)

# Load Cogs
cogs = ['cogs.moderation', 'cogs.utility', 'cogs.airline_pilots', 'cogs.airline_fleet', 'cogs.airline_routes', 'cogs.airline_contracts', 'cogs.pilot_applications']

for cog in cogs:
    bot.load_extension(cog)

@bot.event
async def on_ready():
    logging.info(f'{bot.user.name} has connected to Discord!')

bot.run(TOKEN)