import requests
import settings 
import json
import urllib.parse

agent = requests.Session()
agent.verify = False

url = settings.CRAFTY_API_URL + "/api/v2/servers/" + settings.CRAFTY_SEVER_ID



def requestOptions(method: str = "GET", endpoint: str = ""):
    return {
        "url": f"{url}{endpoint}",
        "headers": {
            "Authorization": f"Bearer {settings.CRAFTY_API_KEY}",
            "Content-Type": "application/json"
        },
        "method": method,
    }


startOption = requestOptions('POST', "/action/start_server")
statsOption = requestOptions('GET', "/stats")


def get_stats():
    return agent.request(**statsOption)

def start_crafty_session():
    pass

def test_crafty():
    response = get_stats()
    print(response.text)

print(url)
test_crafty()