from discord.ext import commands
from discord import app_commands, Interaction

class MySlashCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="slash ping")
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message("pong slash")

async def setup(bot):
    await bot.add_cog(MySlashCog(bot))
