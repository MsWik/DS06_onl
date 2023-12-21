
from math import gcd

class Fraction:
    def __init__(self, num, denum):
        if denum < 0:
            self.num = -num
            self.denum = -denum
        else:
            self.num = num
            self.denum = denum


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
        number.numerator(number.numerator() // common_divisor)
        number.denominator(number.denominator() // common_divisor)
        return number

    def __str__(self):
        return f"{self.num}/{self.denum}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.denum})"

    def __add__(self, other):
        if self.denum == other.denum:
            return Fraction(self.num + other.num, self.denum)
        else:
            new_denum = self.denum * other.denum
            new_num = self.num * other.denum + other.num * self.denum
            return Fraction(new_num, new_denum)




a = Fraction(1, 3)
b = Fraction(1, 2)
c = a + b
print(a, b, c, a is c, b is c)