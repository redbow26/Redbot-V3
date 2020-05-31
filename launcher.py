import logging
from lib.bot import bot

VERSION = "0.0.2"

# Create main logger and handler for discord.py
discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.INFO)
discord_handler = logging.FileHandler(filename="./data/log/discord.log", mode='a')
discord_handler.setFormatter(logging.Formatter(fmt='%(levelname)-8s | %(asctime)-15s | %(name)-15s | %(message)s'))
discord_logger.addHandler(discord_handler)

# Create logger for the bot it self (redbot)
logger = logging.getLogger("redbot")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename="./data/log/redbot.log", mode='a')
handler.setFormatter(logging.Formatter(fmt='%(levelname)-8s | %(asctime)-15s | %(name)-15s | %(message)s'))
logger.addHandler(handler)

bot.run(VERSION)