from discord.ext import commands
import discord
import requests
import settings
import os
import random
import json
import urllib.parse


@commands.command(
    name="hydrus-random",
    aliases=["hyr"],
    help="query a random image from hydrus database",
    enabled=True
)
async def hydrus(ctx):
    async with ctx.typing():

        if ctx.author.id != settings.THE_SHAUS_ID:
            await ctx.send("nu uh")
            return

        API_KEY = settings.HYDRUS_API_KEY
        BASE_URL = settings.HYDRUS_API_URL 
        HEADERS = {"Hydrus-Client-API-Access-Key": API_KEY}

        search_url = f"{BASE_URL}/get_files/search_files"

        tags = [
            ["rating:safe", "rating:general"],
            ["system:has url with class gelbooru file page", "system:has url with class yande.re file page"],
            "-loli",
        ]

        tags = urllib.parse.quote(json.dumps(tags), safe='')

        query = {
            "tags": tags,
            "return_file_ids": True
        }

        filename = None

        try:
            response = requests.post(search_url, json=query, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            file_ids = data.get("file_ids", [])

            if not file_ids:
                await ctx.send("cant find")
                return

            file_id = random.choice(file_ids)

            metadata_url = f"{BASE_URL}/get_files/file_metadata"
            metadata_req = requests.post(metadata_url, json={"file_ids": [file_id]}, headers=HEADERS)
            metadata_req.raise_for_status()
            ext = metadata_req.json()["metadata"][0]["ext"]
            filename = f"temp_hydrus.{ext}"


            file_url = f"{BASE_URL}/get_files/file"
            file_req = requests.get(file_url, headers=HEADERS, params={"file_id": file_id})

            with open(filename, "wb") as f:
                f.write(file_req.content)

            await ctx.send(file=discord.File(filename))

        except Exception as e:
            await ctx.send(f"blueeh: {e}")

        finally:
            if filename and os.path.exists(filename):
                os.remove(filename)

async def setup(bot):
    bot.add_command(hydrus)