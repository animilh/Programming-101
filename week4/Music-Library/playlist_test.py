import unittest
from playlist import Playlist
from song import Song

class PlaylistTest(unittest.TestCase):


    def setUp(self):
        self.mylist = Playlist("Yohoho", shuffle=True)
        self.cool = Song("Bager", "Kokosha Glawa", "Kokosha Glawa", '3:10')
        self.ska = Song("Mor-ska","Q-check","Unknown",'3:12')

    def test_is_instace_of_playlist(self):
        self.assertIsInstance(self.mylist, Playlist)

    def test_has_song_in_list(self):
        song = Song("Hashish from Amsterdam","MFSkasters","Neznam", '4:21')
        self.assertFalse(self.mylist.has_song(song))

    def test_add_song_to_playlist(self):
        self.mylist.add_song(self.cool)
        self.assertTrue(self.mylist.has_song(self.cool))

    def test_remove_song_from_list(self):
        self.mylist.remove_song(self.cool)
        self.assertFalse(self.mylist.has_song(self.cool))

    def test_remove_None_song_from_list(self):
        with self.assertRaises(ValueError):
            self.mylist.remove_song(None)

    def test_add_songs_to_list(self):
        songs = []
        songs.append(self.cool)
        songs.append(self.ska)
        self.mylist.add_songs(songs)
        self.assertTrue(self.mylist.has_song(self.cool))
        self.assertTrue(self.mylist.has_song(self.ska))

    def test_add_songs_empty_to_list(self):
        songs = []
        with self.assertRaises(ValueError):
            self.mylist.add_songs(songs)

    def test_total_length_of_playlist(self):
        songs = [self.cool, self.ska]
        self.mylist.add_songs(songs)
        self.assertEqual(self.mylist.total_length(),'0:06:22')

    def test_artist_dict_of_playlist(self):
        songs = [self.cool, self.ska]
        self.mylist.add_songs(songs)
        expected = {"Kokosha Glawa" : 1, "Q-check" : 1}
        self.assertEqual(self.mylist.artists(), expected)

    def test_get_json_filename_of_list(self):
        expected = 'Yohoho.json'
        self.assertEqual(self.mylist.get_json_filename(), expected)


if __name__ == '__main__':
    unittest.main()
