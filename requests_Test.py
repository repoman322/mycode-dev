
import requests
import json
import yaml


url= "https://opentdb.com/api.php?amount=3&category=11&difficulty=medium"

# GET, POST, PUT, DELETE, PATCH

resp = requests.get(url)

d = resp.json()
print(d["results"][0]["question"])

x = json.dumps(d)

print(type(d))
