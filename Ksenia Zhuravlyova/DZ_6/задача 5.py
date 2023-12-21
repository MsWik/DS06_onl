
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

    def __gt__(self, other):
        return (self.num * other.denum) > (other.num * self.denum)

    def __lt__(self, other):
        return(self.num * other.denum) < (other.num * self.denum)

    def __ge__(self, other):
        return (self.num * other.denum) >= (other.num * self.denum)
    def __le__(self, other):
        return(self.num * other.denum) <= (other.num * self.denum)
    def __eq__(self, other):
        return(self.num * other.denum) == (other.num * self.denum)
    def __ne__(self, other):
        return(self.num * other.denum) != (other.num * self.denum)





a = Fraction(1, 3)
b = Fraction(1, 2)
print(a > b, a < b, a >= b, a <= b, a == b, a != b)


# Вывод
# False True False True False False