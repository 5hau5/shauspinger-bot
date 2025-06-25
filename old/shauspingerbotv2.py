import discord
from discord.ext import commands
from discord import app_commands
import google_currency as google_currency
import json

bot = commands.Bot(command_prefix="//", intents=discord.Intents.all()) 

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="c")
@app_commands.describe(from_="From", to_="To", amount_="Amount")
async def currency_conversion(interaction:discord.Interaction, _from:str, _to:str, _amount:float):

    if  not (0.00000001 < _amount < 999999999999999):
        #await message.channel.send("fuc off")
        print("no")

    else:
        conversion = json.loads(google_currency.convert(_from, _to, _amount))
        if conversion['converted'] == True:
            print(conversion['amount'])


