import discord
from discord.ext import commands
from response_config_handler import *
import settings

class GoofyMsgs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        
        ctx = await self.bot.get_context(message)
        if ctx.valid:
            return
        
        msg_content = message.content.lower()

        response = pick_response(msg_content)
        if response:
            await message.channel.send(response)

        #got pinged
        if (f'<@{self.bot.user.id}>' in message.content):
            await message.channel.send(pick_response(section="got_pinged_text"))
            await message.channel.send(pick_response(section="got_pinged_gif"))



async def setup(bot):
    await bot.add_cog(GoofyMsgs(bot))