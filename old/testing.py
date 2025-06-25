import requests
import json
import urllib.parse
import random
import settings

BASE_URL = "http://127.0.0.1:45869"
API_KEY = "512ef90e855d5238fcd53e712a85266d7737dee2578982129993f57e1ffd6cc6"
#API_KEY = settings.HYDRUS_API_KEY
HEADERS = {"Hydrus-Client-API-Access-Key": API_KEY}

tags = [
            ["rating:safe", "rating:general"],
            ["system:has url with class gelbooru file page", "system:has url with class yande.re file page"],
            "2girls",
        ]


tags_encoded = urllib.parse.quote(json.dumps(tags), safe='')

params = {
    "tags": tags_encoded,
    "return_file_ids": "true",
}

url = f"{BASE_URL}/get_files/search_files"

response = requests.get(url, headers=HEADERS, params=params)
data = response.json()
file_ids = data.get("file_ids", [])
file_id = random.choice(file_ids)

print(file_id)
print(response.status_code)
print(response.text)
