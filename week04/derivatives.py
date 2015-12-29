from sympy import *
import sys


class Polinomial:
    # polinom = sys.argv[1]

    def __init__(self):
        self.poli = sys.argv[1]

    def __str__(self):
        return "The derivative of f(x) = {} is: f'(x) = {}".format(self.simplify(), self.get_derivative())

    def simplify(self):
        if self.poli == '1':
            return 1
        if '1' in self.poli:
            self.poli = self.poli[self.poli.index('1')+4:]
        self.poli = str((simplify(self.poli)).expand()).replace('**', '^')
        return self.poli

    def get_degree(self, new_degree, der_expression, el, coef):
        if new_degree == 1:
            der_expression += str(coef*degree(el)) + '*x'
        if new_degree == 0:
            der_expression += str(degree(el))
            return der_expression
        if new_degree != (0 or 1):
            der_expression += str(coef*degree(el)) + '*x^' + str(new_degree)
        return der_expression

    def get_derivative(self):
        if self.poli == '1':
            return 0
        der_expression = ""
        splitted = self.simplify().split(' + ')
        for el in splitted:
            if el == 'x':
                der_expression += '1'
            new_degree = degree(el) - 1
            if LC(el) == 1 and el != 'x':
                der_expression += self.get_degree(new_degree, der_expression, el, 1)
            if LC(el) != (1) and el != 'x':
                der_expression += self.get_degree(new_degree, der_expression, el, LC(el))
            if splitted.index(el) == (len(splitted) - 1 or len(splitted)):
                return der_expression
            if splitted.index(el) < len(splitted)-1:
                der_expression += ' + '
        return der_expression
