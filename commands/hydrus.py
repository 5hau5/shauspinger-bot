from discord.ext import commands
import discord
import requests
import settings
import os
import random
import json
import urllib.parse
import responses

sus_tags = [
    "bestiality",
    "female furry",
    "furry",
    "futanari",
    "male_focus",
    "pee",
    "peeing",
    "pregnant",
    "trap",
    "yaoi",
    "loli",
    ]

@commands.command(
    name="hydrus-random",
    aliases=["hyr"],
    help="query a random image from shaus hydrus database",
    enabled=True
)
async def hydrus(ctx, *, tag_input: str = ""):
    async with ctx.typing():
        if any(tag in tag_input for tag in sus_tags):
            await ctx.send("nu uh")
            return

        API_KEY = settings.HYDRUS_API_KEY
        BASE_URL = settings.HYDRUS_API_URL 
        HEADERS = {"Hydrus-Client-API-Access-Key": API_KEY}

        search_url = f"{BASE_URL}/get_files/search_files"


        if ctx.message.channel.is_nsfw():
            tags = [
                ["system:has url with class pixiv file page", "system:has url with class gelbooru file page", "system:has url with class yande.re file page"],
                "-loli"
            ]
        else:
            tags = [
                "rating:general",
                ["system:has url with class gelbooru file page", "system:has url with class yande.re file page"],
                "-loli"
            ]



        if tag_input:
            # replace commas with spaces, split into words, replace underscores with spaces
            user_tags = [
                tag.replace("_", " ").strip()
                for tag in tag_input.replace(",", " ").split()
                if tag.strip()
            ]
            print(user_tags)
            tags.extend(user_tags)
        print(tags)

        tags_enc = urllib.parse.quote(json.dumps(tags), safe='')

        query = {
            "tags": tags_enc,
            "return_file_ids": "true"
        }

        filename = None

        try:
            response = requests.get(search_url, params=query, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            file_ids = data.get("file_ids", [])
            print(len(file_ids))

            if not file_ids:
                response = requests.get(search_url, params={"tags":user_tags,"return_file_ids": "true"}, headers=HEADERS)
                data = response.json()
                if data.get("file_ids", []):
                    await ctx.send("no horni")
                else:
                    await ctx.send("cant find")
                return

            file_id = random.choice(file_ids)

            # GET metadata properly
            metadata_url = f"{BASE_URL}/get_files/file_metadata"
            metadata_params = {
                "file_ids": urllib.parse.quote(json.dumps([file_id]), safe='')
            }
            metadata_req = requests.get(metadata_url, params=metadata_params, headers=HEADERS)
            metadata_req.raise_for_status()
            metadata_json = metadata_req.json()["metadata"][0]

            urls = metadata_json.get("known_urls", [])
            page_url = next((url for url in urls if "gelbooru" in url or "yande.re" in url), None)

            if page_url:
                await ctx.send(f"{page_url}")
            else:
                ext = metadata_json["ext"]
                filename = f"temp_hydrus.{ext}"

                file_url = f"{BASE_URL}/get_files/file"
                file_res = requests.get(file_url, headers=HEADERS, params={"file_id": file_id})
                file_res.raise_for_status()

                with open(filename, "wb") as f:
                    f.write(file_res.content)

                await ctx.send(file=discord.File(filename))

        except Exception as e:
            await ctx.send(f"blueeh: {e}")

async def setup(bot):
    bot.add_command(hydrus)