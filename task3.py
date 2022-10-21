import json

import requests

appid = "739630"
r = requests.get(
    "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=" + appid + "&count=3&maxlength=300&format=json")
# print(r.json())
print(json.loads(r.content))
