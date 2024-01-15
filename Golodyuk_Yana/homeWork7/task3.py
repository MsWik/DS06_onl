## 3
# Класс Fraction, который реализует предлагаемые дроби

# методы:

# numerator() — возвращает значение числителя;
# numerator(number) — изменяет значение числителя и производит сокращение дроби, если это необходимо;
# denominator() – возвращает значение знаменателя;
# denominator(number) — изменяет значение знаменателя и производит сокращение дроби, если необходимо;
# __str__ — возвращает строковое представление дроби в формате <числитель>/<знаменатель>;
# __repr__ — возвращает описание объекта в формате Fraction(<числитель>, <знаменатель>).
# оператор математического отрицания — унарный минус
# + — сложение дробей, создаёт новую дробь;
# - — вычитание дробей, создаёт новую дробь;
# += — сложение дробей, изменяет дробь, переданную слева;
# -= — вычитание дробей, изменяет дробь, переданную слева.
# * — умножение дробей, создаёт новую дробь;
# / — деление дробей, создаёт новую дробь;
# *= — умножение дробей, изменяет дробь, переданную слева;
# /= — деление дробей, изменяет дробь, переданную слева.
# Также разработайте метод reverse, возвращающий дробь обратную данной.
# реализация методов сравнения: >, <, >=, <=, ==, !=


def D(x: int) -> set:
    x = abs(x)
    d = set()
    for i in range(1, x + 1):
        if x % i == 0:
            d.add(i)
    return d


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            if "/" in str(args[0]):
                self.num = int(args[0].split("/")[0])
                self.denum = int(args[0].split("/")[1])
            else:
                self.num = int(args[0])
                self.denum = 1
        else:
            self.num = args[0]
            self.denum = args[1]

        if self.num * self.denum >= 0:
            self.num = abs(self.num)
            self.denum = abs(self.denum)
        else:
            self.num = -abs(self.num)
            self.denum = abs(self.denum)

        d_num = D(self.num)
        d_denum = D(self.denum)
        d_od = d_num & d_denum
        d = max(d_od)
        self.num = self.num // d
        self.denum = self.denum // d

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.denum < other.num * self.denum

    def __le__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.denum <= other.num * self.denum

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.denum == other.num * self.denum

    def __gt__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.denum > other.num * self.denum

    def __ge__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.denum >= other.num * self.denum

    def __ne__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return self.num * other.denum != other.num * self.denum

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        obj = Fraction(self.num * other.num, self.denum * other.denum)
        return obj

    def __rmul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        obj = Fraction(self.num * other.num, self.denum * other.denum)
        return obj

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        obj = Fraction(self.num * other.denum, self.denum * other.num)
        return obj

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        obj = Fraction(self.num * other.denum, self.denum * other.num)
        return obj

    def __imul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        self = Fraction(self.num * other.num, self.denum * other.denum)

    def __itruediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        self = Fraction(self.num * other.denum, self.denum * other.num)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        obj = Fraction(
            self.num * other.denum + self.denum * other.num, self.denum * other.denum
        )
        return obj

    def __radd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        obj = Fraction(
            self.num * other.denum + self.denum * other.num, self.denum * other.denum
        )
        return obj

    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        self = Fraction(
            self.num * other.denum + self.denum * other.num, self.denum * other.denum
        )

    def __isub__(self, other):
        self = Fraction(
            self.num * other.denum - self.denum * other.num, self.denum * other.denum
        )

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        obj = Fraction(
            self.num * other.denum - self.denum * other.num, self.denum * other.denum
        )
        return obj

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        obj = Fraction(
            self.num * other.denum - self.denum * other.num, self.denum * other.denum
        )
        return obj

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

    def __str__(self):
        return f"{self.num}/{self.denum}"

    def __repr__(self):
        return f"Fraction('{self.num}/{self.denum}')"

    def __neg__(self):
        neg_obj = Fraction(-self.num, self.denum)
        return neg_obj

    def reverse(self):
        return Fraction(self.denum, self.num)


if __name__ == "__main__":
    # fraction = Fraction(3, 9)
    # print(fraction, repr(fraction))
    # fraction = Fraction("7/14")
    # print(fraction, repr(fraction))

    # a = Fraction(1, 3)
    # b = Fraction(-2, -6)
    # c = Fraction(-3, 9)
    # d = Fraction(4, -12)
    # print(a, b, c, d)
    # print(*map(repr, (a, b, c, d)))

    # a = Fraction(1, 3)
    # b = Fraction(1, 2)
    # c = a + b
    # d = a * b
    # print(a, b, c, d, a is c, b is c)
    # print(a > b, a < b, a >= b, a <= b, a == b, a >= b)

    a = Fraction(1)
    b = Fraction("2")
    c, d = map(Fraction.reverse, (2 + a, -1 + b))
    print(a, b, c, d)
    print(a > b, c > d)
    print(a >= 1, b >= 1, c >= 1, d >= 1)