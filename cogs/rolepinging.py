import discord
from discord.ext import commands
import re
import settings

class RolePinger(commands.Cog):
    """ping shaus for games"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        
        if (('<@&1221754627419017247>' in message.content) or\
            ('<@&1125004823813685358>' in message.content) or\
            ('<@&1223982339730833448>' in message.content) or\
            ('<@&1088083937722634311>' in message.content) or\
            ('<@&738831293588045889>' in message.content) or\
            ('<@&738831293609148416>' in message.content) or\
            ('<@&1224685430897643520>' in message.content) or\
            ('<@&1224885527598071919>' in message.content)) and not\
            ((str(message.author.id) == f'{settings.THE_SHAUS_ID}') and not ('<@&1224885527598071919>' in message.content)): #shaus and not @test

            games = re.findall('<@&(.+?)>', message.content)
            msg = re.sub(r"<@&.*>", "", message.content)
            #print(msg)
            #print(games)
            role = ''
            for game in games:
                #print (game)
                role = role + ' ' + str(discord.utils.get(message.guild.roles, id=int(game)))
                #print('role is', role)  

            await message.channel.send(f'<@{settings.THE_SHAUS_ID}> '+ role + msg)


async def setup(bot):
    await bot.add_cog(RolePinger(bot))