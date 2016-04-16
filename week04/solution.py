import sys
from collections import OrderedDict


class Polynomial:

    def __init__(self):
        self.poli = sys.argv[1]
        self.poli_dict = OrderedDict()

    def generate_poli_dict(self):
        split_by_plus = self.poli.split('+')
        split_by_plus = [el.strip() for el in split_by_plus]
        for elem in split_by_plus:
            try:
                if int(elem) in range(1, 10):
                    self.poli_dict[elem] = "0"
            except:
                if elem == 'x':
                    self.poli_dict[elem] = "1"
                else:
                    split_by_multiply = ["x"+e if "^" in e else e for e in elem.split("x")]
                    coef = split_by_multiply[0]
                    if coef == '':
                        coef = "1"
                    try:
                        x_power = split_by_multiply[1]
                    except:
                        x_power = coef
                        coef = 1
                    if x_power in self.poli_dict:
                        self.poli_dict[x_power] = int(self.poli_dict[x_power]) + int(coef)
                    else:
                        self.poli_dict[x_power] = coef
        self.poli_dict = OrderedDict(reversed(sorted([key for key in self.poli_dict.items()])))
        return self.poli_dict


class Derivative:

    def __init__(self, dict_obj):
        self.polynom = dict_obj
        self.der_dict = OrderedDict()

    def __str__(self):
        return "The derivative of f(x) = {} is:\nf'(x) = {}".\
            format(self.normalize_to_str(self.polynom), self.normalize_to_str(self.der_dict))

    def calc_derivative(self):
        for elem in self.polynom:
            if self.polynom[elem] != "0":
                if elem == 'x':
                    self.der_dict[elem] = "1proizv"
                    return self.der_dict
                old_coef = int(self.polynom[elem])
                old_degree = int(elem[elem.index('^'):].replace('^', ''))
                variable = elem[:elem.index('^')]
                new_degree = str(variable) + '^' + str(old_degree - 1)
                self.der_dict[new_degree] = old_degree*old_coef

            else:
                self.der_dict[elem] = "0proizv"
        return self.der_dict

    def normalize_to_str(self, dictt):
        deriv_str = ""
        for elem in dictt:
            if dictt[elem] != "0proizv":
                if dictt[elem] == "1proizv":
                    deriv_str += "1"
                elif dictt[elem] == "0":
                    deriv_str += elem
                    return deriv_str
                elif dictt[elem] == "0":
                    deriv_str += "0"
                elif dictt[elem] == "1" and elem == 'x':
                    deriv_str += "x"
                else:
                    deriv_str += str(dictt[elem]) + '*' + str(elem)
                if elem is not list(dictt.keys())[-1]:
                    deriv_str += ' + '
            else:
                deriv_str = deriv_str.replace("1*", "")
                deriv_str = deriv_str.replace("+", "")
                if len(dictt) == 1:
                    deriv_str = "0"
            deriv_str = deriv_str.replace("^1", "")
        return deriv_str


def main():
    polynomial = Polynomial()
    generated = polynomial.generate_poli_dict()
    deriv = Derivative(generated)
    deriv.calc_derivative()
    print(deriv.__str__())


if __name__ == '__main__':
    main()
