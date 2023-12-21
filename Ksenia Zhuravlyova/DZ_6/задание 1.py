
from math import gcd

class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            parts = args[0].split('/')
            self.num = int(parts[0])
            self.denum = int(parts[1])
        elif len(args) == 2:
            self.num = args[0]
            self.denum = args[1]
        else:
            raise ValueError("Invalid number of arguments")

    def numerator(self, number=None):
        if not number:
            return self.num
        else:
            self.num = number

    def denominator(self, number=None):
        if not number:
            return self.denum
        else:
            self.denum = number

    @staticmethod
    def drobi(number):
        common_divisor = gcd(number.numerator(), number.denominator())
        simplified_fraction = Fraction(number.numerator() // common_divisor, number.denominator() // common_divisor)
        return simplified_fraction

    def __str__(self):
        return f"{self.num}/{self.denum}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.denum})"

fraction = Fraction(3, 9)
print(fraction, repr(fraction))
simplified_fraction = Fraction.drobi(fraction)
print(simplified_fraction, repr(simplified_fraction))

fraction = Fraction('7/14')
print(fraction, repr(fraction))
simplified_fraction = Fraction.drobi(fraction)
print(simplified_fraction, repr(simplified_fraction))