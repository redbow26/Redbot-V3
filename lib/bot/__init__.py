# Generic/Built-in

# Other Libs
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound

# Other Imports
from ..db import db

PREFIX = "." # Prefix constant
OWNER_IDS = [175990133240233984] # List of owner ids

class Bot(BotBase):
	"""
	Summary line

		TODO:
			* Do the docstring
    """
	def __init__(self):
		"""

        """
		self.PREFIX = PREFIX
		self.ready = False
		# self.guild = None # Single server 
		self.scheduler = AsyncIOScheduler() #

		db.autosave(self.scheduler)
		super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

	def run(self, version):
		"""
		Start and run the bot
	  
	        Parameters: 
		        version (string): String to define the version of the bot
		"""
		self.VERSION = version

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
		print("Bot connected")

	async def on_disconnect(self):
		"""
		Summary line

			TODO:
				* Do the docstring
	    """
		print("Bot disconnected")

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
			self.ready = True
			# self.guild = self.get_guild(549103172275404810) # Single server 
			self.scheduler.start()


			print("bot ready")
		else:
			print("bot reconnected")

	async def on_message(self, message):
		"""
		Summary line

			TODO:
				* Do the docstring
	    """
		pass


bot = Bot()