import json
from pathlib import Path


directory = 'C:\\Code\\Spotipy\\spotipy\\workspace\\spotipy\\songs_files'
data = []
files = Path(directory).glob('*')
for file in files:
    with open(file) as f:
        data.append(json.load(f))
