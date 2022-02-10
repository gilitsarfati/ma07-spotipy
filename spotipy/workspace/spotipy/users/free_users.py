
from workspace.spotipy.config.configuration import Configuration
from workspace.spotipy.music.playlists import Playlist
from workspace.spotipy.music.songs import Song
from workspace.spotipy.users.all_users import AllUsers


class FreeUsers(AllUsers):
    def __init__(self, user_name, password, user_id):
        AllUsers.__init__(user_name, password, user_id)
        self.config = Configuration()

    def add_playlist(self, new_playlist: Playlist):
        if not self.if_token(new_playlist) and len(self.playlists) < self.config.max_playlists and len(new_playlist.songs) < self.config.max_songs_per_playlists:
            self.playlists.append(new_playlist)
        else:
            print("this name is already token! too much playlists/ songs in playlist")

    def add_song_to_playlist(self, playlist: Playlist, song: Song):
        if len(playlist.songs) < self.config.max_songs_per_playlists:
            playlist.songs.append(song)
        else:
            print("too much songs")
