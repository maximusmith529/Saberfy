import random

from SpotifyAPI import SpotifyAPI
import json


class node:
    def __init__(self, time, lineIndex, lineLayer, type, cutDirection):
        self.time = time
        self.lineIndex = lineIndex
        self.lineLayer = lineLayer
        self.type = type
        self.cutDirection = cutDirection


def writeDiff(songID):
    spotify = SpotifyAPI("b6709a08f53d40b6ab740ff646c017a6", "110e1f30d2f3463a8b56a06a528fbcb7")
    songDetails = spotify.get_analysis(songID)
    tatumList = []
    for x in songDetails["tatums"]:
        tatumList.append(x)

    nodeList = [];

    posToDir = {tuple([0, 2]): tuple([0, 4, 8]), tuple([3, 2]): tuple([0, 5, 8]),
                tuple([0, 1]): tuple([0, 1, 4, 8]), tuple([3, 1]): tuple([0, 1, 3, 8]),
                tuple([0, 0]): tuple([1, 6, 8]), tuple([3, 0]): tuple([1, 7, 8]),
                tuple([1, 2]): tuple([0, 3, 8]), tuple([2, 2]): tuple([0, 2, 8]),
                tuple([1, 1]): tuple([3, 8]), tuple([2, 1]): tuple([2, 8]),
                tuple([1, 0]): tuple([1, 3, 8]), tuple([2, 0]): tuple([1, 2, 8])}
    counter = 0;
    for x in tatumList:
        xax = random.randint(0, 1)
        yax = random.randint(0, 2)

        possibleLDir = posToDir.get(tuple([xax, yax]))
        ind = random.randint(0, len(possibleLDir) - 1)
        # left one
        nodeTemp = node(x["start"], xax, yax, 0, possibleLDir[ind])
        nodeList.append(nodeTemp)

        xax = 3-xax
        possibleRDir = posToDir.get(tuple([xax, yax]))
        # right one
        nodeTemp = node(x["start"], xax, yax, 1, possibleRDir[ind])
        nodeList.append(nodeTemp)
        counter = counter + 1

    fullString = ""
    for x in nodeList:
        tempString = "{\"_time\": " + str(x.time) + ",\"_lineIndex\": " + str(x.lineIndex) + ",\"_lineLayer\": " + str(
            x.lineLayer) + ",\"_type\": " + str(x.type) + ",\"_cutDirection\": " + str(x.cutDirection) + "},"
        fullString = fullString + str(tempString);
    fullString = str(fullString.rstrip(fullString[-1]))

    diffString = "{\"_version\": \"2.6.0\",\"_notes\":[" + fullString + "],\"_sliders\": [],\"_obstacles\": [],\"_events\": [],\"_waypoints\": []}"

    diffJson = json.loads(diffString)

    with open("temp/Normal.dat", "w") as outfile:
        outfile.write(diffString)

    # diff = json.dumps(
    #     {
    #     "_version": "2.6.0",
    #     "_notes": [fullString.repalce("\","")],
    #     "_sliders": [], 
    #     "_obstacles": [],
    #     "_events": [],
    #     "_waypoints": []
    #     }
    # )
    # with open("Normal.dat", "w") as outfile:
    #     outfile.write(diff)
