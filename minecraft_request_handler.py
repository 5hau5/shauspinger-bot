from discord.ext import commands
import requests
import settings
import json
import urllib.parse
import re
import asyncio

api_url = re.sub(r'/$', '', settings.CRAFTY_API_URL)
server_url = api_url + "/api/v2/servers/" + settings.CRAFTY_SEVER_ID

#print(server_url)

agent = requests.Session()
agent.verify = False

def requestOptions(
        url: str= "", 
        method: str = "GET", 
        endpoint: str = "",
        bearer_token: str = settings.CRAFTY_API_KEY
        ):
    
    return {
        "url": f"{url}{endpoint}",
        "headers": {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        },
        "method": method,
    }

statsOption = requestOptions(server_url, 'GET', "/stats")
startOption = requestOptions(server_url, 'POST', "/action/start_server")
endOption = requestOptions(server_url, 'POST', "/action/stop_server")

async def get_status():
    loop = asyncio.get_running_loop()

    # run blocking request in executor
    resp = await loop.run_in_executor(
        None,
        lambda: agent.request(**statsOption)
    )

    data = resp.json()

    if "data" in data and "icon" in data["data"]:
            del data["data"]["icon"]

    return json.dumps(data, indent=2)

async def start_server():
    loop = asyncio.get_running_loop()

    # run blocking request in executor
    resp = await loop.run_in_executor(
        None,
        lambda: agent.request(**startOption)
    )

    data = resp.json()

    print (data)
    return data

async def stop_server():
    loop = asyncio.get_running_loop()

    # run blocking request in executor
    resp = await loop.run_in_executor(
        None,
        lambda: agent.request(**endOption)
    )
    data = resp.json()

    print (data)
    return data