import numbs
import unittest


class NumbsTestCase(unittest.TestCase):

    def test_is_even(self):
        self.assertTrue(numbs.is_even(2))
        self.assertFalse(numbs.is_even(3))

    def test_is_odd(self):
        self.assertFalse(numbs.is_odd(2))
        self.assertTrue(numbs.is_odd(3))

    def test_is_composite(self):
        self.assertFalse(numbs.is_composite(3))
        self.assertTrue(numbs.is_composite(4))

    def test_is_prime(self):
        self.assertTrue(numbs.is_prime(3))
        self.assertFalse(numbs.is_prime(4))


if __name__ == '__main__':
    unittest.main()
