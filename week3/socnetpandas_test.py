import unittest
from socnetpandas import Panda, PandaSocialNetwork
import re

class SocialNetPandasTest(unittest.TestCase):
    genders = ['male','female']

    def setUp(self):
        self.ani = Panda("Ani", "ani@pandamail.com", "female")
        self.net = PandaSocialNetwork()
        self.net.add_panda(self.ani)
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



if __name__ == '__main__':
    unittest.main()
# import re
# def email():
#     email = raw_input("enter the mail address::")
#      match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)

#     if match:
#         print "valid email :::", match.group()
#     else:
#         print "not valid:::"

# email()
