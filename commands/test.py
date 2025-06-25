from discord.ext import commands
import discord

@commands.command(
    name="test",
    help="a place holder command",
    enabled=True
)
async def test(
    ctx,
    param1 = commands.parameter(default=None, description="parameter 1")
):
    await ctx.send("test")

async def setup(bot):
    bot.add_command(test)