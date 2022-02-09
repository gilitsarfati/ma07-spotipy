from workspace.spotipy.music.singers import Singer


class Album:
    def __init__(self, album_id, name, singer_id):
        self.album_id = album_id
        self.name = name
        self.singer_id: Singer.singer_id = singer_id

