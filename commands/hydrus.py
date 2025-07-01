from discord.ext import commands
import requests
import settings
import random
import json
import urllib.parse

sus_tags = [
    "furry",
    "futanari",
    "pee",
    "peeing",
    "trap",
    "yaoi",
    ]

wtf_tags = [
    "bestiality",
    "pregnant",
]

def encode(tags):
    return urllib.parse.quote(json.dumps(tags), safe='')

@commands.command(
    name="hydrus-random",
    aliases=["hyr"],
    help="query a random image from shaus hydrus database",
    enabled=True
    )
async def hydrus(
    ctx, 
    *, tag_input: str= commands.parameter(default='', description='Tags separated by either spaces or commas')
    ):
    async with ctx.typing():
        file_limit = 5

        cleaned_input = tag_input 
        user_tags = []

        if tag_input:

            user_tags = [
            tag.replace("_", " ").strip()
            for tag in cleaned_input.replace(",", " ").split()
            if tag.strip()
            ]


            if any(tag in user_tags for tag in sus_tags):
                await ctx.send("nu uh")
                return

            if any(tag in user_tags for tag in wtf_tags):
                await ctx.send(f"<@{settings.THE_SHAUS_ID}> give me ability to ban")
                return

        # tags for nsfw and sfw or sfw
        tags_base = [
            f"system:limit={file_limit}",
            [
                "system:has url with class pixiv file page",
                "system:has url with class gelbooru file page",
                "system:has url with class yande.re file page",
                "system:has url with class zzz - renamed due to auto-import - x post"
            ],
            "-loli",
        ]

        tags_sfw = [
            f"system:limit={file_limit}",
            "rating:general",
            [
                "system:has url with class gelbooru file page",
                "system:has url with class yande.re file page"
            ],
            "-loli",
        ]

        tags_to_use = tags_base if ctx.channel.is_nsfw() else tags_sfw

        # parse user tags if any
        if user_tags:
             tags_to_use.extend(user_tags)

        print(tags_to_use)

        API_KEY = settings.HYDRUS_API_KEY
        BASE_URL = settings.HYDRUS_API_URL 
        HEADERS = {"Hydrus-Client-API-Access-Key": API_KEY}

        search_url = f"{BASE_URL}/get_files/search_files"

        query = {
            "file_sort_type":4, #random
            "tags": encode(tags_to_use),
            "return_file_ids": "true",   
        }

        try:
            response = requests.get(search_url, params=query, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            #print(data)
            file_ids = data.get("file_ids", [])
            print(file_ids)

            if not file_ids:
                if ctx.message.channel.is_nsfw():
                    await ctx.send("cant find")
                    return

                query["tags"] = encode([["rating:explicit", "rating:sensitive", "rating:questionable"], "-loli"]) # set to allow only nsfw to see if any is there
                response = requests.get(search_url, params=query, headers=HEADERS)
                data = response.json()

                if data.get("file_ids", []):
                    await ctx.send("no horni here")
                else:
                    await ctx.send("cant find")
                return
            
            #file_id = random.choice(file_ids)
            file_id = file_ids[0]

            metadata_url = f"{BASE_URL}/get_files/file_metadata"
            metadata_params = {
                "file_ids": encode([file_id])
            }
            metadata_req = requests.get(metadata_url, params=metadata_params, headers=HEADERS)
            metadata_req.raise_for_status()
            metadata_json = metadata_req.json()["metadata"][0]

            urls = metadata_json.get("known_urls", [])
            page_url = next(
                (url for url in urls if "gelbooru" in url or "yande.re" in url or "pixiv" in url or "x post" in url), 
                None
                )

            await ctx.send(f"{page_url}")

        except Exception as e:
            await ctx.send(f"blueeh: {e}")

async def setup(bot):
    bot.add_command(hydrus)