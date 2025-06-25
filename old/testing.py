import requests
import json
import urllib.parse

BASE_URL = "http://127.0.0.1:45869"
API_KEY = "512ef90e855d5238fcd53e712a85266d7737dee2578982129993f57e1ffd6cc6"
HEADERS = {"Hydrus-Client-API-Access-Key": API_KEY}

tags = ["rating:safe", "rating:general", "-blue_eyes"]
tags_json = json.dumps(tags)
tags_encoded = urllib.parse.quote(tags_json, safe='')

params = {
    "tags": tags_encoded,
    "return_file_ids": "true",
    "file_sort_type": 6,
    "file_sort_asc": "false"
}

url = f"{BASE_URL}/get_files/search_files"

response = requests.get(url, headers=HEADERS, params=params)

print(response.status_code)
print(response.text)
