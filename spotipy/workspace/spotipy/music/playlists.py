from workspace.spotipy.music.songs import Song


class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        self.songs: list[Song] = []

    def add_song_to_playlist(self, song: Song):
        self.songs.append(song)

    def remove_song_from_playlist(self, song: Song):
        self.songs.remove(song)
