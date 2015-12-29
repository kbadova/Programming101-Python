import unittest
from derivatives import Polinomial
from sympy import *


class TestPolinomial(unittest.TestCase):

    def setUp(self):
        self.polinomial = Polinomial('2*x^2 + x^2')
        # self.polinomial.poli = 'x^3 + 10*x^3'

    def test__str__(self):
        self.assertEqual(self.polinomial.__str__(), "The derivative of f(x) = 3*x^2 is: f'(x) = 6*x")

    def test_simplify(self):
        self.assertEqual(self.polinomial.simplify(), '1')

    def test_derivative(self):
        self.assertEqual(self.polinomial.get_derivative(), '0')

if __name__ == '__main__':
    unittest.main()

