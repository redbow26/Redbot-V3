from discord.ext.commands import Cog

class Fun(Cog):
	"""
	Summary line

		TODO:
			* Do the docstring
    """
    
	def __init__(self, bot):
		"""
		Summary line
			
			Parameters: 
			        bot (discord.ext.commands.bot): Bot discord 

			TODO:
				* Do the docstring
	    """
		self.bot = bot

	@Cog.listener()
	async def on_ready(self):
		"""
		Summary line

			TODO:
				* Do the docstring
	    """
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("fun")


def setup(bot):
	bot.add_cog(Fun(bot))