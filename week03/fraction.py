from fractions import gcd


class Fractions:

    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return "{} / {}".format(self.num, self.denom)

    def __repr__(self):
        return self.__str__()

    def simplify(self, obj):
        divisor = gcd(obj.num, obj.denom)
        obj.num /= divisor
        obj.denom /= divisor
        return str(Fractions(int(obj.num), int(obj.denom)))

    def sum_of_fraction(self, second):
        denom = self.denom * second.denom
        num = self.num * second.denom + second.num * self.denom
        if num == denom:
            return '1'
        return self.simplify(Fractions(num, denom))

    def subtract_of_fraction(self, second):
        denom = self.denom * second.denom
        num = self.num * second.denom - second.num * self.denom
        if num == denom:
            return '1'
        if num == 0:
            return '0'
        return self.symplify(Fractions(num, denom))

    def multiply(self, second):
        return self.simplify(Fractions(self.num * second.num, self.denom * second.denom))

    def __eq__(self, other):
        return self.simplify(self) == self.simplify(other)

