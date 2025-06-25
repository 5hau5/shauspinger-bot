import discord
from discord.ext import commands
from responses import *
import settings

class GoofyMsgs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        #r6s
        if ('<@&738831293588045889>' in message.content):
            await message.channel.send(respond(r6_ping_responses))
        
        #sex
        if ('sex' in message.content.lower()) or\
            ('segs' in message.content.lower()) or\
            ('seggs' in message.content.lower()):
            await message.channel.send('https://cdn.discordapp.com/attachments/738831293864738975/1229998157941833758/segs-arona.gif?ex=6631b80d&is=661f430d&hm=08dce8539c48abe0a9ccbefb101cd9309fff33148e35b546facda55cbf4fae2e&')
        
        #r6s
        if ('seeg' in message.content.lower()):
            pass

        #got pinged
        if ('<@1224676688521199616>' in message.content) and (settings.PREFIX not in message.content):
            await message.channel.send(respond(get_pinged_responses_1))
            await message.channel.send(respond(get_pinged_responses_2))



async def setup(bot):
    await bot.add_cog(GoofyMsgs(bot))