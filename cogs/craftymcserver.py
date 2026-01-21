from discord.ext import commands
import requests
import settings
import json
import urllib.parse
import re
import asyncio
from minecraft_request_handler import *

class CraftyMCServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.allowed_users = settings.ALLOWED_MC_CMD_USERS

    @commands.group(
        name="minecraft-server",
        aliases=["mc"],
        invoke_without_command=True
    )
    async def minecraft_server(self, ctx):
        await ctx.send("Use a subcommand like `status`, `start` or `stop`")



    @minecraft_server.command(
        name="status",
        aliases=["st", "s", "--status", "-st", "-s"]
    )
    async def minecraft_server_status(self, ctx):
        #clean dis shit up
        data = await get_status()
        await ctx.send(f"```json\n{data}\n```")


    
    @minecraft_server.command(
        name="start",
        aliases=["-start", "--start"]
    )
    async def start_minecraft_server(self, ctx):
        if ctx.author.id not in self.allowed_users:
            return await ctx.send("no")
        
        resp = await start_server()
        data = await get_status()
        #await ctx.send(f"```json\n{data}\n```")

    
    @minecraft_server.command(
        name="stop",
        aliases=["-stop", "--stop"]
    )
    async def stop_minecraft_server(self, ctx):
        if ctx.author.id not in self.allowed_users:
            return await ctx.send("no")
        
        resp = await stop_server()
        data = await get_status()
        #await ctx.send(f"```json\n{data}\n```")


async def setup(bot):
    await bot.add_cog(CraftyMCServer(bot))