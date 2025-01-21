import os
import urllib.request
import json
from pprint import pprint

#clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

url = "https://graph.facebook.com/facebook/picture?redirect=false"
#url = "http://search.twitter.com/search.json?q=python&rpp=1"
response = urllib.request.urlopen(url)
raw_data = response.read()
#print(raw_data)

data = json.loads(raw_data)

pprint(data)

#for x in data["data"]["url"].split("/"):
#    print(x)

#==============================================================================

url = "http://graph.facebook.com/111974415485969/picture?type=large"
response = urllib.request.urlopen(url)
raw_data = response.read()

# Open the file in binary write mode
with open("profile_image.png", "wb") as image:
    image.write(raw_data)
    image.close()
