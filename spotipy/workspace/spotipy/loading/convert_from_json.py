import json
from pathlib import Path


def convert_to_songs():
    directory = 'C:\\Code\\Spotipy\\spotipy\\workspace\\spotipy\\songs_files'
    songs = []
    files = Path(directory).glob('*')
    for file in files:
        with open(file) as f:
            songs.append(json.load(f))
    return songs


print(convert_to_songs())
