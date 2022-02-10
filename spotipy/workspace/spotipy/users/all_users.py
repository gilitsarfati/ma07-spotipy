from typing import List

from workspace.spotipy.music.playlists import Playlist
from workspace.spotipy.searching.search import Search


class AllUsers:
    def __init__(self, user_name, password, user_id):
        self.user_name = user_name
        self.password = password
        self.user_id = user_id
        self.playlists: List[Playlist] = []

    def if_token(self, new_playlist: Playlist):
        for playlist in self.playlists:
            if playlist.playlist_name == new_playlist.playlist_name:
                return True
        return False

    def add_playlist(self, new_playlist: Playlist):
        if not self.if_token(new_playlist):
            self.playlists.append(new_playlist)
        else:
            print("this name is already token!")

