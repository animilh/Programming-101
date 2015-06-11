import unittest
import realdeal


class RealDealTest(unittest.TestCase):


    def test_sum_of_divisors(self):
        self.assertEqual(realdeal.sum_of_divisors(8), 15)

    def test_is_prime(self):
        self.assertTrue(realdeal.is_prime(13))

    def test_is_not_prime(self):
        self.assertFalse(realdeal.is_prime(14))

    def test_prime_numbers_of_divisors_false(self):
        self.assertFalse(realdeal.prime_number_of_divisors(8))

    def test_prime_numbers_of_divisors_true(self):
        self.assertTrue(realdeal.prime_number_of_divisors(9))

    def test_contains_digit_true(self):
        self.assertTrue(realdeal.contains_digit(1237, 7))

    def test_contains_digit_false(self):
        self.assertFalse(realdeal.contains_digit(1237, 8))

    def test_contains_digits_true(self):
        self.assertTrue(realdeal.contains_digits(1237, [7, 2]))

    def test_contains_digits_false(self):
        self.assertFalse(realdeal.contains_digits(1237, [8, 1]))

    def test_is_number_balanced_true(self):
        self.assertTrue(realdeal.is_number_balanced(1238033))

    def test_is_number_balanced_false(self):
        self.assertFalse(realdeal.is_number_balanced(28471))

    def test_count_substrings(self):
        self.assertEqual(realdeal.count_substrings("This is a test string", "is"), 2)


    def test_zero_insert(self):
        self.assertEqual(realdeal.zero_insert(116457), 10160457)

    def test_sum_matrix(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(realdeal.sum_matrix(m), 45)




if __name__ == '__main__':
    unittest.main()
