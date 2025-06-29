from discord.ext import commands
import discord
import random   
import settings
import os
from response_config_handler import *

image_dir = os.path.join(settings.RESOURCE_DIR, 'goofy_aa_big_head_images')
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

@commands.command(
    name="goofy_aa_big_head",
    aliases=["gabh"],
    help="post a goofy aa big head image",
    enabled=True
)
async def goofy_aa_big_head(ctx):
    if not image_files:
        raise Exception(f"no images found in {image_dir}")

    random_image_file = random.choice(image_files)
    image_path = os.path.join(image_dir, random_image_file)
    await ctx.send(pick_response(section="goofy_aa_big_head"))
    await ctx.send(file=discord.File(image_path))

async def setup(bot):
    bot.add_command(goofy_aa_big_head)