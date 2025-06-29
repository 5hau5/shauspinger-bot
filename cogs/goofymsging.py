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

        #r6s
        # if ('<@&738831293588045889>' in message.content):
        #     await message.channel.send(respond(r6_ping_responses))
        

        #got pinged
        # if ('<@1224676688521199616>' in message.content) and (settings.PREFIX not in message.content):
        #     await message.channel.send(respond(get_pinged_responses_1))
        #     await message.channel.send(respond(get_pinged_responses_2))



async def setup(bot):
    await bot.add_cog(GoofyMsgs(bot))