import os
import mutagen.id3
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from song import Song
from playlist import Playlist


class Crawler:

    file_types = ('mp3','ogg')

    def __init__(self, path):
        self.path = os.path.abspath(path)

    def get_id3_tags(self, file_path):
        result = {}
        try:
            audio = MP3(file_path, ID3=EasyID3)
            result['artist'] = audio['artist'][0]
            result['title'] = audio['title'][0]
            result['album'] = audio['album'][0]
            result['length'] = audio.info.length
            return result
        except mutagen.id3.error:
            pass

    def generate_playlist(self):
        files_in_dir = [filename for filename in os.listdir(self.path) if filename.endswith(Crawler.file_types)]
        my_list = Playlist(name="Yohoho", repeat=False, shuffle=False)
        for music_file in files_in_dir:
            tags = self.get_id3_tags(str(self.path + '/' + music_file))
            my_list.add_song(Song(tags['title'], tags['artist'], tags['album'], tags['length']))
        return my_list

def main():
    crawler = Crawler('/home/burnaski/Music')
    playlist = crawler.generate_playlist()
    for song in playlist:
        print('{} - {} length {}').format(song.title(), song.artist(), song.length())

if __name__ == '__main__':
    main()
