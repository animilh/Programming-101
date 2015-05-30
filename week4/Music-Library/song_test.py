import unittest
from song import Song


class SongTest(unittest.TestCase):


    def setUp(self):
        self.mysong = Song('Chicho', "Review", "Unknown", '3:30')


    def test_is_instance_of_song(self):
        self.assertIsInstance(self.mysong, Song)


    def test_str_representation_of_song(self):
        self.assertEqual(str(self.mysong), "Review - Chicho from Unknown - 3:30")


    def test_equal_songs(self):
        song = Song("Chicho", "Review", "Unknown", '3:30')
        self.assertEqual(self.mysong, song)


    def test_not_equal_songs(self):
        song = Song("Should I stay or should I go", "Clash", "London's calling", '3:43')
        self.assertNotEqual(self.mysong, song)


    def test_value_error_in_length(self):
        with self.assertRaises(ValueError):
            song = Song("Chicho", "Review", "Unknown", '3.30')
            song.length_song(minutes=True)


    def test_length_song_in_minutes(self):
        self.assertEqual(self.mysong.length_song(minutes=True), 3.5)


    def test_length_song_in_seconds(self):
        self.assertEqual(self.mysong.length_song(seconds=True), 210)


if __name__ == '__main__':
    unittest.main()

