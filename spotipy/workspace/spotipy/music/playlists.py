from workspace.spotipy.music.songs import Song


class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs: list[Song] = []
