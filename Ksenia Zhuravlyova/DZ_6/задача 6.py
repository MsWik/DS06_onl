
from math import gcd

class Fraction:
    def __init__(self, num, denum=1):
        if isinstance(num, str):
            parts = num.split('/')
            if len(parts) == 2:
                self.num = int(parts[0])
                self.denum = int(parts[1])
            else:
                self.num = int(num)
                self.denum = denum
        elif isinstance(num, int):
            self.num = num
            self.denum = denum

    @staticmethod
    def reverse(fraction):
        return Fraction(fraction.denum, fraction.num)

    def simplify(self):
        common_divisor = gcd(self.num, self.denum)
        self.num = self.num // common_divisor
        self.denum = self.denum // common_divisor

    def __str__(self):
        return f"{self.num}/{self.denum}"

    def __repr__(self):
        return f"Fraction('{self.num}/{self.denum}')"

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denum + other.num * self.denum
            new_denum = self.denum * other.denum
            return Fraction(new_num, new_denum)
        elif isinstance(other, (int, str)):
            other = Fraction(other)
            return self + other
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denum - other.num * self.denum
            new_denum = self.denum * other.denum
            return Fraction(new_num, new_denum)
        elif isinstance(other, (int, str)):
            other = Fraction(other)
            return self - other
        else:
            raise TypeError("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.num
            new_denum = self.denum * other.denum
            return Fraction(new_num, new_denum)
        elif isinstance(other, (int, str)):
            other = Fraction(other)
            return self * other
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denum
            new_denum = self.denum * other.num
            return Fraction(new_num, new_denum)
        elif isinstance(other, (int, str)):
            other = Fraction(other)
            return self / other
        else:
            raise TypeError("Unsupported operand type")

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denum == other.num * self.denum
        elif isinstance(other, (int, str)):
            other = Fraction(other)
            return self == other
        else:
            raise TypeError("Unsupported operand type")

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denum > other.num * self.denum
        elif isinstance(other, (int, str)):
            other = Fraction(other)
            return self > other
        else:
            raise TypeError("Unsupported operand type")

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denum >= other.num * self.denum
        elif isinstance(other, (int, str)):
            other = Fraction(other)
            return self >= other
        else:
            raise TypeError("Unsupported operand type")

    def __lt__(self, other):
        if isinstance (other, Fraction):
            return self.num * other.denum < other.num * self.denum
        elif isinstance(other, (int, str)):
            other = Fraction(other)
            return self < other
        else:
            raise TypeError("Unsupported operand type")

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denum <= other.num * self.denum
        elif isinstance(other, (int, str)):
            other = Fraction(other)
            return self <= other
        else:
            raise TypeError("Unsupported operand type")



a = Fraction(1)
b = Fraction('2')
c, d = map(Fraction.reverse, (a + 2, b - 1))
print(a, b, c, d)
print(a > b, c > d)
print(a >= 1, b >= 1, c >= 1, d >= 1)

# Вывод
# 1/1 2/1 1/3 1/1
# False False
# True True False True