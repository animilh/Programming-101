from decimal import Decimal

class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)


    def __repr__(self):
        return self.__str__()


    def __add__(self, other):
        return Fraction(self.numerator*other.denominator + self.denominator*other.numerator, self.denominator * other.denominator).syk()


    def __sub__(self, other):
        return Fraction(self.numerator*other.denominator - self.denominator*other.numerator, self.denominator * other.denominator).syk()


    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator).syk()


    def __div__(self, other):
        return Fraction(self.numerator * other.denumirator, self.denominator * other.nominator).syk()

    def __eq__(self, other):
        return Decimal(self.numerator / self.denominator) == Decimal(other.numerator / other.denominator)

    def syk(self):
        return '{}.{}'.format(self.numerator/self.denominator, self.numerator%self.denominator)
