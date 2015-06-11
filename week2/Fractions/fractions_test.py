import unittest
from fractions import Fraction


class FractionsTest(unittest.TestCase):

    def setUp(self):
        self.frac = Fraction(1, 2)
        self.other = Fraction(1, 3)

    def test_is_instance_of_fractions(self):
        self.assertIsInstance(self.frac, Fraction)

    def test_fraction_with_zero_denominator(self):
        with self.assertRaises(ValueError):
            num = Fraction(2, 0)

    def test_str_fraction(self):
        expected = '1/2'
        self.assertTrue(str(self.frac) == expected)

    def test_add_fractions(self):
        self.assertEqual(self.frac.__add__(self.other), Fraction(5, 6))

    def test_sub_fractions(self):
        self.assertEqual(self.frac.__sub__(self.other), Fraction(1, 6))

    def test_mul_fractions(self):
        self.assertEqual(self.frac.__mul__(self.other), Fraction(1, 6))

    def test_div_fractions(self):
        self.assertEqual(self.frac.__div__(self.other), Fraction(3, 2))

    def test_equal_fractions(self):
        self.assertTrue(self.frac.__eq__(Fraction(1, 2)))

    def test_not_equal_fractions(self):
        self.assertFalse(self.frac.__eq__(self.other))


if __name__ == '__main__':
    unittest.main()
