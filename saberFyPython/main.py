from SpotifyAPI import SpotifyAPI
import json
import spotdl
import os
from infoWriter import infoWriter
from node import writeDiff

if __name__ == '__main__':
    spotify = SpotifyAPI("b6709a08f53d40b6ab740ff646c017a6", "110e1f30d2f3463a8b56a06a528fbcb7")

    input = input("please enter a spotify url\n")

    uri = input.split("/")[len(input.split("/"))-1];

    songDetails = spotify.get_analysis(uri)
    writeDiff(uri)
    iw = infoWriter(uri, 0)
    iw.write()

    os.system("spotdl https://open.spotify.com/track/"+uri+" --output-format ogg --output temp/ --path-template song.{ext}")












