
from SpotifyAPI import SpotifyAPI
import json

from infoWriter import infoWriter

if __name__ == '__main__':
    infoW = infoWriter("0ZNqGbEclCmKtyw3l4RrM0?si=fdce999a2bad4b6a")
    infoW.getInfo()
    infoW.writeInfo()

    """
    json_object = json.dumps(songDetails, indent=4)

    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    """










