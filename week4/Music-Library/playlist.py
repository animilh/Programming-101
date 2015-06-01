from datetime import timedelta
import random
from tabulate import tabulate
from song import Song
import json

class Playlist:

    def __init__(self, name, repeat=False,shuffle=False):
        self.name = name
        self.playlist = []
        self.repeat = repeat
        self.shuffle = shuffle
        self.__current_song_index = 0
        self.__shuffle_played_songs = set()

    def __str__(self):
        for song in self.playlist:
            return "{} - {}".format(song.title(), song.length())

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return iter(self.playlist)



    def add_song(self, song):
        if song is None:
            raise ValueError("No song to add")
        self.playlist.append(song)

    def has_song(self, song):
        return song in self.playlist

    def remove_song(self, song):
        if song is None:
            raise ValueError("No song to remove")
        if song in self.playlist:
            self.playlist.remove(song)
        else:
            print ("No such song in playlist {}".format(self.name))

    def add_songs(self, songs):
        if songs == [] or songs == None:
            raise ValueError("No list of songs to add")
        self.playlist.extend(songs)

    def total_length(self):
        totalsec=sum([song.length_song(seconds = True) for song in self.playlist])
        return str(timedelta(seconds = totalsec))

    def artists(self):
        all_artists=[song.artist() for song in self.playlist]
        return {name : all_artists.count(name) for name in all_artists}

    def _shuffle(self):
        song = random.choice(self.playlist)
        while song in self.__shuffle_played_songs:
            song = random.choice(self.playlist)
        self.__shuffle_played_songs.add(song)

    def pprint_playlist(self):
        headers = ["Artist", "Song", "Length"]
        table = []
        for song in self.playlist:
            table.append([song.artist(), song.title(), song.length()])
        print(tabulate(table, headers = headers, tablefmt="fancy_grid"))

    def get_json_filename(self):
        return self.name.replace(" ", "-") + ".json"

    def save(self):
        data = {
               "name": self.name,
               "playlist": [song.__dict__ for song in self.playlist]
               }
        with open(self.get_json_filename(), 'w') as f:
            f.write(json.dumps(data, indent=True))

    @staticmethod
    def load(filename):
        with open(filename, 'r') as f:
            content = json.load(f)
            p = Playlist(content["name"])
            for song in content["playlist"]:
                new_song = Song(
                    artist=song["_Song__artist"], title=song["_Song__title"], album=song["_Song__album"], length=song["_Song__length"])
                p.add_song(new_song)
            return p
