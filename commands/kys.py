from discord.ext import commands
import settings

@commands.command(    
    name="kys",
    help="es",
    enabled=True
)
async def kys(ctx):
    if ctx.author.id == settings.THE_SHAUS_ID or ctx.author.id == settings.MILO_ID: 
        await ctx.send("bluehh")
        await ctx.bot.close_bot()
    else:
        await ctx.send("nu uh")

async def setup(bot):
    bot.add_command(kys)