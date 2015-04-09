import unittest
from socnetpandas import Panda, PandaSocialNetwork
import re

class SocialNetPandasTest(unittest.TestCase):
    genders = ['male','female']

    def setUp(self):
        self.ani = Panda("Ani", "ani@pandamail.com", "female")
        self.deni = Panda("Deni", "deni@pandamail.com", "female")
        self.emil = Panda("Emo", "emo@pandamail.com", "male")
        self.tosho = Panda("Tosho", "tosho@pandamail.com", "male")
        self.net = PandaSocialNetwork()
        for panda in [self.deni, self.ani, self.emil, self.tosho]:
            self.net.add_panda(panda)

        self.net.make_friends(self.ani, self.deni)
        self.net.make_friends(self.ani, self.emil)
        self.net.make_friends(self.tosho, self.deni)
        print ("Starting Up")


    def tearDown(self):
        print ("Tearing Down")


    def test_instance_of_panda_class(self):
        self.assertIsInstance(self.ani, Panda)


    def test_gender_panda(self):
        self.assertIn(self.ani.gender(),self.genders)

    def test_invalid_gender_panda(self):
        with self.assertRaises(ValueError):
            test = Panda("Test", "test@pandamail.com", "ffemale")

    def test_valid_email_panda(self):
        self.assertTrue(re.search(r'[\w.-]+@[\w.-]+.\w+', self.ani.email()))

    def test_invalid_email_panda(self):
        with self.assertRaises(ValueError):
            test = Panda("Test", "&test@pandamail.com", "ffemale")

    def test_string_panda(self):
        expected = "Panda Ani, email ani@pandamail.com, gender female"
        self.assertEqual(str(self.ani), expected)

    def test_equal_pandas(self):
        fani = Panda("Ani", "ani@pandamail.com", "female")
        self.assertEqual(self.ani, fani)

    def test_put_panda_in_dict(self):
        d = {}
        d[self.ani] = []
        self.assertIn(self.ani, d)

    def test_instance_of_panda_social_network(self):
        self.assertIsInstance(self.net.network, dict)


    def test_add_panda_in_network(self):
        self.assertTrue(self.net.has_panda(self.ani))

    def test_has_panda_in_network(self):
        self.assertTrue(self.net.has_panda(self.ani))

    def test_panda_already_in_network(self):
        with self.assertRaises(Exception):
            self.net.add_panda(self.ani)

    def test_panda_not_in_network(self):
        with self.assertRaises(Exception):
            self.net.add_panda(self.fani)

    def test_make_friends_pandas_in_network(self):
        fani = Panda("Fani", "fani@pandamail.com", "female")
        self.net.make_friends(self.ani, fani)
        self.assertIn(self.ani, self.net[fani])
        self.assertIn(fani, self.net[self.ani])

    def test_pandas_are_already_friends(self):
        with self.assertRaises(Exception):
            self.net.make_friends(self.ani, self.deni)

    def test_pandas_are_friends(self):
        self.assertTrue(self.net.are_friends(self.ani, self.deni))

    def test_pandas_are_not_friends(self):
        sani = Panda("Sani", "sani@pandamail.com", "female")
        self.assertFalse(self.net.are_friends(sani,self.ani))

    def test_friends_of_panda_in_network(self):
        self.assertEqual(self.net.friends_of(self.ani), [self.deni, self.emil])

    def test_friends_of_panda_not_in_network(self):
        sani = Panda("Sani", "sani@pandamail.com", "female")
        self.assertFalse(self.net.friends_of(sani))

    def test_connection_level_between_pandas_in_network(self):
        self.assertTrue(self.net.connection_level(self.ani, self.deni) == \
            self.net.connection_level(self.ani, self.emil) == \
                self.net.connection_level(self.tosho, self.deni) == 1)
        self.assertTrue(self.net.connection_level(self.ani, self.tosho) == 2)

    def test_connection_level_between_pandas_not_in_network(self):
        sani = Panda("Sani", "sani@pandamail.com", "female")
        shani = Panda("Shani", "shani@pandamail.com", "female")
        self.assertFalse(self.net.connection_level(sani, shani))

    def test_connection_level_if_pandas_are_not_connected(self):
        sani = Panda("Sani", "sani@pandamail.com", "female")
        self.net.add_panda(sani)
        self.assertEqual(self.net.connection_level(sani, self.ani), -1)

    def test_are_connected_pandas(self):
        self.assertNotIn(self.net.are_connected(self.ani, self.emil), (-1, 'False'))

    def test_find_friend_at_level_in_network(self):
        expected = self.net.find_friend(1, self.ani)
        self.assertEqual(self.net.find_friend(1, self.ani), expected)

    def test_how_many_gender_in_network(self):
        self.assertEqual(self.net.how_many_gender_in_network(2, self.ani, "male"), 2)

    def test_how_many_gender_in_network_if_level_lessthan_one(self):
        with self.assertRaises(ValueError):
            self.net.how_many_gender_in_network(0, self.ani, "male")

    def test_how_mani_gender_in_network_if_bad_gender(self):
        with self.assertRaises(ValueError):
            self.net.how_many_gender_in_network(0, self.ani, "mamale")

if __name__ == '__main__':
    unittest.main()
