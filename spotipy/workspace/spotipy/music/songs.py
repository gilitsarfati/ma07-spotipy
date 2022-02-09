from workspace.spotipy.music.albums import Album
from workspace.spotipy.music.singers import Singer


class Song:
    def __init__(self, song_id, name, popularity, album, singers):
        self.song_id = song_id
        self.name = name
        self.popularity = popularity
        self.album: Album = album
        self.singers: list[Singer] = singers
