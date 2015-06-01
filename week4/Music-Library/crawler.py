import os
import datetime
import mutagen.id3
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from song import Song
from playlist import Playlist

class Crawler:

    file_types = ('mp3','ogg')

    def __init__(self, path):
        self.path = os.path.abspath(path)

    def get_id3_tags(self, audio):
        result = {}
        result['artist'] = audio['artist'][0]
        result['title'] = audio['title'][0]
        result['album'] = audio['album'][0]
        result['length'] = str(datetime.timedelta(seconds=int(audio.info.length)))
        return result


    def generate_playlist(self):
        files_in_dir = [filename for filename in os.listdir(self.path) if filename.endswith(Crawler.file_types)]
        my_list = Playlist(name="Yohoho", repeat=False, shuffle=False)
        for music_file in files_in_dir:
            try:
                audio = MP3(self.path + '/' + music_file, ID3=EasyID3)
                tags = self.get_id3_tags(audio)
                my_list.add_song(Song(tags['title'], tags['artist'], tags['album'], tags['length']))
            except mutagen.id3.error:
                continue
        return my_list

def main():
    crawler = Crawler('/home/burnaski/Music')
    playlist = crawler.generate_playlist()
    print(playlist)

if __name__ == '__main__':
    main()
