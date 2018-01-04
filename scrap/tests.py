import requests as r
import json

url = "https://api2.spir.ai/home/header"

sess = r.Session()
req = sess.get(url)
data = req.json()

with open("data.json", 'w') as file:
    json.dump(data, file)

























