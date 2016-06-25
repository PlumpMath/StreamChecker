import json
from urllib.request import urlopen
import string
import os, time

twitchBase = "https://api.twitch.tv/kraken/streams/"

def getStreams():
    streamList = []
    with open("streams.json") as json_file:
        json_data = json.load(json_file)
    for x in range(0, len(json_data["streams"])):
        streamList.append(json_data["streams"][x]["streamURL"])
    return streamList

def get_jsonparsed_data(url):
    return json.loads(str((urlopen(url)).read()).encode('ascii','ignore').decode('unicode_escape')[2:-1])

def printStreams(i, streams):
    for x in range(0, len(streams)):
        urlToCheck = twitchBase + streams[x]
        response = get_jsonparsed_data(urlToCheck)
        if i == 1:
            if(response["stream"] != None):
                print("[%d] " %(x+1) + (streams[x]) + " is active")
            else:
                print("[%d] " %(x+1) + (streams[x]) + " is not active")
        if i == 2:
            if(response["stream"] != None):
                print("[%d] " %(x+1) + (streams[x]) + " is active")
        if i == 3:
            if(response["stream"] == None):
                print("[%d] " %(x+1) + (streams[x]) + " is not active")
            
            
    


def mainLoop(streams):
    print("[1] See all streams\n[2] See active streams\n[3] See offline streams")
    userChoice = 0
    secondChoice = 0
    while userChoice != '1' and userChoice != '2' and userChoice != '3':
        userChoice = input("Please select an option: ")

    if userChoice == '1':
        printStreams(1, streams)
        print("Select a stream to play: ")
        secondChoice = input()
        os.system('livestreamer twitch.tv/%s best' %(streams[int(secondChoice)]))
    elif userChoice == '2':
        printStreams(2, streams)
        print("Select a stream to play: ")
        secondChoice = input()
        os.system('livestreamer twitch.tv/%s best' %(streams[int(secondChoice)]))
    elif userChoice == '3':
        printStreams(3, streams)
        

while True:
    mainLoop(getStreams())

##for x in range(0, len(json_data["streams"])):
##    urlToCheck = twitchBase + json_data["streams"][x]["streamURL"]
##    response = get_jsonparsed_data(urlToCheck)
##    if(response["stream"] != None):
##        print((json_data["streams"][x]["streamURL"]) + " is active")
##        os.system('livestreamer twitch.tv/%s best' %(json_data["streams"][x]["streamURL"]))
##    else:
##        print((json_data["streams"][x]["streamURL"]) + " is not active")
    

