from workspace.spotipy.loading.convert_from_json import convert_to_songs


class Search:
    def __init__(self):
        self.all_songs = convert_to_songs()

    def all_singers(self):
        singers = []
        for song in self.all_songs:
            for singer in song["track"]["artists"]:
                if singer not in singers:
                    singers.append(singer)
        return singers

    def search_singer_albums(self, singer_id):
        albums = []
        for song in self.all_songs:
            for singer in song["track"]["artists"]:
                if singer["id"] == singer_id:
                    albums.append(song["track"]["album"])
        return albums

    def by_popularity(self):
        return self["track"]["popularity"]

    def sort_by_popularity(self, singer_id):
        songs_by_singer = []
        for song in self.all_songs:
            for singer in song["track"]["artists"]:
                if singer["id"] == singer_id:
                    songs_by_singer.append(song)
        songs_by_singer.sort(key=self.by_popularity)
        return songs_by_singer

    def most_popular(self, singer_id):
        popular = []
        songs_by_singer = self.sort_by_popularity(singer_id)
        for i in range(10):
            popular.append(songs_by_singer[i])
        return popular

    def songs_in_album(self, album_id):
        songs_in_album = []
        for song in self.all_songs:
            if album_id == song["track"]["album"]["id"]:
                songs_in_album.append(song)
        return songs_in_album


search = Search()
print(search.all_singers())
