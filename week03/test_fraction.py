import unittest
from fraction import Fractions


class TestFraction(unittest.TestCase):

    def setUp(self):
        self.first_frac = Fractions(1, 2)
        self.second_frac = Fractions(2, 5)

    def test_sum_of_fraction(self):
        self.assertEqual(self.first_frac.sum_of_fraction(self.second_frac), '1')

    def test_subtract_of_fractions(self):
        self.assertEqual(self.first_frac.subtract_of_fraction(self.second_frac), '0')

    def test_simplify(self):
        self.assertEqual(self.first_frac.multiply(self.second_frac) , '1 / 4')

    def test__eq__(self):
        third_frac = Fractions(1, 2)
        self.assertNotEqual(self.first_frac, self.second_frac)
        self.assertEqual(self.first_frac, third_frac)


if __name__ == '__main__':
    unittest.main()
