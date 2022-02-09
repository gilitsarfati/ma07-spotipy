from workspace.spotipy.music.songs import Song
from workspace.spotipy.users.all_users import AllUsers


class PremiumUsers(AllUsers):
    def __init__(self, user_name, password):
        AllUsers.__init__(self, user_name, password)

    def add_song_to_playlist(self, song: Song):
        self.songs.append(song)

    def remove_song_from_playlist(self, song: Song):
        self.songs.remove(song)
