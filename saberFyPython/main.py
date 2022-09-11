from SpotifyAPI import SpotifyAPI
import os
from infoWriter import infoWriter
import node
import pathlib
import zipfile


if __name__ == '__main__':
    spotify = SpotifyAPI("b6709a08f53d40b6ab740ff646c017a6", "110e1f30d2f3463a8b56a06a528fbcb7")
    if os.listdir("temp/") != []:
        for i in os.listdir("temp/"):
            os.remove("temp/"+i)
    input = input("please enter a spotify url\n")

    uri = input.split("/")[len(input.split("/"))-1];



    songDetails = spotify.get_analysis(uri)
    node.writeNorm(uri)
    node.writeHard(uri)
    iw = infoWriter(uri, 1.202)
    iw.write()

    directory = pathlib.Path("temp/")
# https://open.spotify.com/track/0AzD1FEuvkXP1verWfaZdv?si=472e19519fb0469f

    os.system("spotdl https://open.spotify.com/track/"+uri+" --output-format ogg --output temp/ --path-template song.{ext}")

    with zipfile.ZipFile("song.zip", mode="w") as archive:
        for file_path in directory.iterdir():
            archive.write(file_path, arcname=file_path.name)











