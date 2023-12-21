
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

a = Fraction(1, 3)
b = Fraction(-2, -6)
c = Fraction(-3, 9)
d = Fraction(4, -12)

a = a.drobi(a)
b = b.drobi(b)
c = c.drobi(c)
d = d.drobi(d)

print(a, b, c, d)
print(*map(repr, (a, b, c, d)))