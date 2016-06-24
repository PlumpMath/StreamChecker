import json
from urllib.request import urlopen
import string
import os, time

twitchBase = "https://api.twitch.tv/kraken/streams/"

with open("streams.json") as json_file:
    json_data = json.load(json_file)

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = str(response.read())
    data = data.encode('ascii','ignore').decode('unicode_escape')
    data = data[2:-1]
    return json.loads(data)

for x in range(0, len(json_data["streams"])):
    urlToCheck = twitchBase + json_data["streams"][x]["streamURL"]
    response = get_jsonparsed_data(urlToCheck)
    if(response["stream"] != None):
        print((json_data["streams"][x]["streamURL"]) + " is active")
        os.system('livestreamer twitch.tv/%s best' %(json_data["streams"][x]["streamURL"]))
    else:
        print((json_data["streams"][x]["streamURL"]) + " is not active")
    

