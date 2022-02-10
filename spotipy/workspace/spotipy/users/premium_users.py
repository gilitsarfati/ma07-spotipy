from workspace.spotipy.music.playlists import Playlist
from workspace.spotipy.music.songs import Song
from workspace.spotipy.users.all_users import AllUsers


class PremiumUsers(AllUsers, Playlist):
    def __init__(self, user_name, password, user_id, playlist_name):
        AllUsers.__init__(self, user_name, password, user_id)
        Playlist.__init__(playlist_name)