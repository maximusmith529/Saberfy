import pathlib
import zipfile
directory = pathlib.Path("temp/")


with zipfile.ZipFile("song.zip", mode="w") as archive:
    for file_path in directory.iterdir():
        archive.write(file_path, arcname=file_path.name)
with zipfile.ZipFile("song.zip", mode="r") as archive:
    archive.printdir()