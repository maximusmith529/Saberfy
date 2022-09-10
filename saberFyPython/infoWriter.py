import json
from SpotifyAPI import SpotifyAPI
class infoWriter():
    songid = None
    songName = None
    artistName = None
    BPM = None

    def __init__(self, songid):
        self.songid = songid

    def getArtist(self):
        spotify = SpotifyAPI("b6709a08f53d40b6ab740ff646c017a6", "110e1f30d2f3463a8b56a06a528fbcb7")
        songDetails = spotify.get_track(self.songid)
        self.artistName = songDetails["artists"][0]["name"]

    def writeInfoDat(self):
        test = json.dumps({
            '_version':'2.6.0',
            '_songName': self.songName,
            '_songSubName': "",
            '_songAuthorName': self.artistName,
            '_levelAuthorName': "saberFy",
            '_beatsPerMinute': self.BPM,
            '_shuffle': 0,
            '_shufflePeriod': 0.5,
            '_previewStartTime': 31.5,
            '_previewDuration': 7,
            '_songFilename': "song.ogg",
            '_coverImageFilename': "cover.jpg",
            '_environmentName': "BigMirrorEnvironment",
            '_allDirectionsEnvironmentName': "GlassDesertEnvironment",
            '_songTimeOffset': 0,
            '_difficultyBeatmapSets': []
        })
        print(test)



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