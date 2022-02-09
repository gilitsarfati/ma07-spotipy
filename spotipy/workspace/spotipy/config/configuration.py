import json


class Configuration:
    with open('configuration.json', 'r') as config_file:
        data = json.load(config_file)

    max_playlists = data['max_playlists']
    max_songs_per_playlists = data['max_songs_per_playlist']
