
from SpotifyAPI import SpotifyAPI
import json
from infoWriter import infoWriter

if __name__ == '__main__':
    spotify = SpotifyAPI("b6709a08f53d40b6ab740ff646c017a6", "110e1f30d2f3463a8b56a06a528fbcb7")

    input = input("please enter a spotify url\n")

    uri = input.split("/")[len(input.split("/"))-1];


    songDetails = spotify.get_analysis(uri)

    songTracks = spotify.get_track(uri)

    infoW = infoWriter(uri, 0)
    infoW.write()












