import unittest
import warmup


class WarmUpTest(unittest.TestCase):

    def test_factorial(self):
        self.assertTrue(warmup.factorial(4) == 24)

    def test_fibonacci(self):
        expected = [1, 1, 2, 3, 5]
        self.assertEqual(warmup.fibonacci(5), expected)

    def test_sum_of_digits(self):
        self.assertEqual(warmup.sum_of_digits(123), 6)
        self.assertEqual(warmup.sum_of_digits(1325132435356),43)

    def test_fact_digits(self):
        self.assertEqual(warmup.fact_digits(999),1088640)

    def test_is_palindrome(self):
        self.assertTrue(warmup.palindrome("kapak"))

    def test_is_not_palindrome(self):
        self.assertFalse(warmup.palindrome("kapaka"))

    def test_to_digits(self):
        self.assertEqual(warmup.to_digits(123023), [1, 2, 3, 0, 2, 3])

    def test_to_number(self):
        self.assertEqual(warmup.to_number([1,2,3,0,2,3]), 123023)

    def test_fib_number(self):
        self.assertEqual(warmup.fib_number(3), 112)

    def test_count_vowels(self):
        self.assertEqual(warmup.count_vowels("Theistareykjarbunga"), 8)

    def test_count_consonants(self):
        self.assertEqual(warmup.count_consonants("Theistareykjarbunga"), 11)

    def test_char_histogram(self):
        self.assertEqual(warmup.char_histogram("AAAAaaa!!!"), { 'A': 4, 'a': 3, '!': 3 })

    def test_is_palindrome_score(self):
        self.assertEqual(warmup.p_score(121), 1)

    def test_is_not_palindrome_score(self):
        self.assertEqual(warmup.p_score(48), 3)

    def test_is_increasing_seq(self):
        self.assertTrue(warmup.is_increasing([1,2,3,4,5]))

    def test_is_not_increasing_seq(self):
        self.assertFalse(warmup.is_increasing([1,2,3,4,5,1]))

    def test_is_decreasing_seq(self):
        self.assertTrue(warmup.is_decreasing([5,4,3,2,1]))

    def test_is_not_decreasing_seq(self):
        self.assertFalse(warmup.is_decreasing([1, 2, 3, 4, 5, 1]))

    def test_next_hack_number(self):
        self.assertEqual(warmup.next_hack(8031), 8191)



if __name__ == '__main__':
    unittest.main()
