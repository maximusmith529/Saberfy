
from SpotifyAPI import SpotifyAPI
import json

from infoWriter import infoWriter

if __name__ == '__main__':
    spotify = SpotifyAPI("b6709a08f53d40b6ab740ff646c017a6", "110e1f30d2f3463a8b56a06a528fbcb7")
    songDetails = spotify.get_analysis("0a9sd6MEXZXIPHk0fAxpZ4?si=17c820600f7b4b1e")



    song_json = json.dumps(songDetails, indent=4)
    with open("songDetails.json", "w") as outfile:
        outfile.write(song_json)
    

    infoW = infoWriter("0ZNqGbEclCmKtyw3l4RrM0?si=fdce999a2bad4b6a", 0)
    infoW.write()












