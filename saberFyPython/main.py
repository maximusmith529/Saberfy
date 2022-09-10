
from SpotifyAPI import SpotifyAPI
import json

if __name__ == '__main__':
    spotify = SpotifyAPI("b6709a08f53d40b6ab740ff646c017a6", "110e1f30d2f3463a8b56a06a528fbcb7")
    songDetails = spotify.get_analysis("0AzD1FEuvkXP1verWfaZdv?si=6972a6aa2c4a4036")

    songTracks = spotify.get_track("4lv9Fj6md6hbu6eavN8EKa?si=a2d8bf3e51544820")
    for i in songTracks["artists"]:
        print(i)

    cover = songTracks["album"]["images"][0]


"""
song_json = json.dumps(songTracks, indent=4)
with open("songdetail.json", "w") as outfile:
    outfile.write(song_json)

"""





