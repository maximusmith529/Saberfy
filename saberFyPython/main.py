from http.server import HTTPServer

from SpotifyAPI import SpotifyAPI
import json
import spotdl
import os
from infoWriter import infoWriter
from node import writeDiff
import pathlib
import zipfile
from server import MyServer
from http.server import BaseHTTPRequestHandler

if __name__ == '__main__':
    spotify = SpotifyAPI("b6709a08f53d40b6ab740ff646c017a6", "110e1f30d2f3463a8b56a06a528fbcb7")
    webServer = HTTPServer(("localhost", 8080), MyServer)
    print("Server started http://localhost:8080")

    while  not len(MyServer.path) == (23):
        webServer.handle_request()

    webServer.server_close()
    print("Server stopped.")

    if os.listdir("temp/") != []:
        for i in os.listdir("temp/"):
            os.remove("temp/"+i)
   # input = input("please enter a spotify url\n")

    uri = MyServer.path.split("/")[1] #input.split("/")[len(input.split("/"))-1];
    print("the uri is"+uri)

    songDetails = spotify.get_analysis(uri)
    writeDiff(uri)
    iw = infoWriter(uri, 1.202)
    iw.write()

    directory = pathlib.Path("temp/")
# https://open.spotify.com/track/0AzD1FEuvkXP1verWfaZdv?si=472e19519fb0469f

    os.system("spotdl " + input + " --output-format ogg --output temp/ --path-template song.{ext}")

    with zipfile.ZipFile("song.zip", mode="w") as archive:
        for file_path in directory.iterdir():
            archive.write(file_path, arcname=file_path.name)













