import json
from SpotifyAPI import SpotifyAPI
import requests


class infoWriter():
    songid = None
    songName = None
    artistName = None
    cover = None
    music = None
    BPM = None
    offset = None
    songLength = None

    def __init__(self, songid, offset):
        self.songid = songid
        self.offset = offset

    def getInfo(self):
        spotify = SpotifyAPI("b6709a08f53d40b6ab740ff646c017a6", "110e1f30d2f3463a8b56a06a528fbcb7")
        songDetails = spotify.get_track(self.songid)
        songAnalysis = spotify.get_analysis(self.songid)
        self.artistName = songDetails["artists"][0]["name"]
        self.songName = songDetails["name"]
        self.cover = songDetails["album"]["images"][0]
        self.songLength = round(songDetails["duration_ms"] / 1000)
        self.BPM = round(songAnalysis["track"]["tempo"])

    def write(self):
        self.getInfo()
        self.writeInfo()
        self.writeImage()

    def writeInfo(self):
        info = json.dumps({
            '_version': '2.6.0',
            '_songName': self.songName,
            '_songSubName': "",
            '_songAuthorName': self.artistName,
            '_levelAuthorName': "saberFy Automated Map",
            '_beatsPerMinute': self.BPM,
            '_shuffle': 0,
            '_shufflePeriod': 0.5,
            '_previewStartTime': self.songLength / 2,
            '_previewDuration': 7,
            '_songFilename': "song.ogg",
            '_coverImageFilename': "cover.jpg",
            '_environmentName': "BigMirrorEnvironment",
            '_allDirectionsEnvironmentName': "GlassDesertEnvironment",
            '_songTimeOffset': self.offset,
            '_difficultyBeatmapSets': [{
                '_difficulty': "Normal",
                '_difficultyRank': 3,
                '_beatmapFilename': "Normal.dat",
                '_noteJumpMovementSpeed': 13,
                '_noteJumpStartBeatOffset': 0
            }]
        })
        with open("temp/Info.dat", "w") as outfile:
            outfile.write(info)

    def writeImage(self):
        img_data = requests.get(self.cover["url"]).content
        with open('temp/cover.jpg', 'wb') as handler:
            handler.write(img_data)


"""
{
  "_version": "2.6.0",
  "_songName": "Example Song",
  "_songSubName": "",
  "_songAuthorName": "Song Artist",
  "_levelAuthorName": "You",
  "_beatsPerMinute": 120,
  "_shuffle": 0,
  "_shufflePeriod": 0.5,
  "_previewStartTime": 31.5,
  "_previewDuration": 7,
  "_songFilename": "song.ogg",
  "_coverImageFilename": "cover.jpg",
  "_environmentName": "BigMirrorEnvironment",
  "_allDirectionsEnvironmentName" : "GlassDesertEnvironment",
  "_songTimeOffset": 0,
  "_difficultyBeatmapSets": [
    // Difficulty beatmap sets (and difficulty beatmaps) are explained later down the page.
    // Check the sidebar!
  ]
}
"""
