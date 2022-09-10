
from SpotifyAPI import SpotifyAPI
import json
import spotdl
import os
from infoWriter import infoWriter
from node import writeDiff

if __name__ == '__main__':

    songid = "46hnqCPtSB5Hz6P3Hh642v?si=24bc6be594d14323"
    writeDiff(songid)
    iw = infoWriter(songid, 0)
    iw.write()

    os.system("spotdl https://open.spotify.com/track/"+songid+" --output-format ogg --output temp/ --path-template song.{ext}")












