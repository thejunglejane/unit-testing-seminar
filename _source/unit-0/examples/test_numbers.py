import numbers
import unittest


class NumbersTestCase(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(numbers.is_even(2))
        self.assertFalse(numbers.is_even(3))

    def test_is_odd(self):
        self.assertFalse(numbers.is_odd(2))
        self.assertTrue(numbers.is_odd(3))

    def test_is_composite(self):
        self.assertFalse(numbers.is_composite(3))
        self.assertTrue(numbers.is_composite(4))

    def test_is_prime(self):
        self.assertTrue(numbers.is_prime(3))
        self.assertFalse(numbers.is_prime(4))


if __name__ == '__main__':
    unittest.main()
