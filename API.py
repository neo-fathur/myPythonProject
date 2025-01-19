#clear the screen
import os
os.system('cls' if os.name == 'nt' else 'clear')

import urllib.request
url = "https://graph.facebook.com/facebook/picture?redirect=false"
response = urllib.request.urlopen(url)
raw_data = response.read()
#print(raw_data)

import json
data = json.loads(raw_data)

from pprint import pprint
#pprint(data)

for x in data["data"]["url"].split("/"):
    print(x)