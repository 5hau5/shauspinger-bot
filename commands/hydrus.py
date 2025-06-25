from discord.ext import commands
import discord
import requests
import settings

@commands.command(
    name="hydrus",
    aliases=["hy"],
    help="query a random image from hydrus database",
    enabled=True
)
async def test(
    ctx,
):
    await ctx.send("test")

async def setup(bot):
    bot.add_command(test)