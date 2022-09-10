
from SpotifyAPI import SpotifyAPI
import json

if __name__ == '__main__':
    spotify = SpotifyAPI("b6709a08f53d40b6ab740ff646c017a6", "110e1f30d2f3463a8b56a06a528fbcb7")
    songDetails = spotify.get_analysis("0AzD1FEuvkXP1verWfaZdv?si=6972a6aa2c4a4036")

    songTracks = spotify.get_track("4lv9Fj6md6hbu6eavN8EKa?si=a2d8bf3e51544820")

    test = json.dumps({
        '_version': '2.6.0',
        '_songName': "test",
        '_songSubName': "",
        '_songAuthorName': "test",
        '_levelAuthorName': "saberFy",
        '_beatsPerMinute': 120,
        '_shuffle': 0,
        '_shufflePeriod': 0,
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







