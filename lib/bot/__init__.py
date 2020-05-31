# Generic/Built-in
from glob import glob
from asyncio import sleep
import logging

# Other Libs
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound

# Other Imports
from ..db import db

PREFIX = "." # Prefix constant
OWNER_IDS = [175990133240233984] # List of owner ids
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")] # List of all the cogs

# Get logger
# TODO: Do logger system
discord_logger = logging.getLogger('discord')
logger = logging.getLogger("redbot")

class Ready(object):
	"""
	Summary line

		TODO:
			* Do the docstring
	"""
	def __init__(self):
		"""
		Summary line

			TODO:
				* Do the docstring
		"""
		for cog in COGS:
			setattr(self, cog, False)

	def ready_up(self, cog):
		"""
		Summary line

			Parameters: 
				cog (string): Cog who need to set ready 

			TODO:
				* Do the docstring
		"""
		setattr(self, cog, True)
		print(f" {cog} cog ready")

	def all_ready(self):
		"""
		Summary line

			TODO:
				* Do the docstring
		"""
		return all([getattr(self, cog) for cog in COGS])


class Bot(BotBase):
	"""
	Summary line

		TODO:
			* Do the docstring
	"""
	def __init__(self):
		"""Initialise new bot"""
		self.PREFIX = PREFIX
		self.ready = False
		self.cogs_ready = Ready()

		# self.guild = None # Single server 
		self.scheduler = AsyncIOScheduler() #

		db.autosave(self.scheduler)
		super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)


	def setup(self):
		for cog in COGS:
			self.load_extension(f"lib.cogs.{cog}")
			print(f" {cog} cog loaded")

		print("setup complete\n")

	def run(self, version):
		"""
		Start and run the bot
	
			Parameters: 
				version (string): Define the version of the bot
		"""
		self.VERSION = version

		print("running setup...")
		self.setup()

		with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
			self.TOKEN = tf.read() # Read the token from "./lib/bot/token.0"

		print("running bot...")
		super().run(self.TOKEN, reconnect=True)


	async def on_connect(self):
		"""
		Summary line

			TODO:
				* Do the docstring
		"""
		print(" bot connected")

	async def on_disconnect(self):
		"""
		Summary line

			TODO:
				* Do the docstring
		"""
		print("bot disconnected")

	async def on_error(self, err, *args, **kwargs):
		"""
		Summary line

			Parameters: 
				err (): 
				*args: Variable length argument list.
				**kwargs: Arbitrary keyword arguments.

			TODO:
				* Do the docstring
		"""
		if err == "on_command_error":
			await args[0].send("Something went wrong.")

		raise


	async def on_command_error(self, ctx, exc):
		"""
		Summary line
		
			Parameters: 
				ctx ():
				exc ():

			TODO:
				* Do the docstring
		"""
		if isinstance(exc, CommandNotFound):
			pass

		elif hasattr(exc, "original"):
			raise exc.original

		else:
			raise exc


	async def on_ready(self):
		"""
		Summary line

			TODO:
				* Do the docstring
		"""
		if not self.ready:
			# self.guild = self.get_guild(549103172275404810) # Single server 
			self.scheduler.start()

			while not self.cogs_ready.all_ready():
				await sleep(0.5)

			self.ready = True
			print(" bot ready")
		else:
			print(" bot reconnected")

	async def on_message(self, message):
		"""
		Summary line

			TODO:
				* Do the docstring
		"""
		if not message.author.bot:
			await self.process_commands(message)


bot = Bot()