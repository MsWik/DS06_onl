import math
from typing import Union


class Fractional:
    def __init__(self, *args) -> None:
        if len(args) == 1:
            self._denum = 1
            if isinstance(args[0], int):
                self._num = args[0]
            elif "/" not in args[0]:
                self._num = int(args[0])
            else:
                self._num = int(args[0].split("/")[0])
                self._denum = int(args[0].split("/")[1])
        else:
            self._num = args[0]
            self._denum = args[1]
        if self._denum == 0:
            raise ValueError("Divison by zero")
        self._sign = -1 if self._num * self._denum < 0 else 1
        self._denum = abs(self._denum)
        self._num = abs(self._num)
        self.slice()

    def __str__(self) -> str:
        if self._denum == 1:
            return f"{self._sign*self._num}"
        return f"{self._sign*self._num}/{self._denum}"

    def __repr__(self) -> str:
        return f"Fraction({self._sign*self._num}, {self.denum})"

    def __radd__(self, object: Union["Fractional", int, str]) -> "Fractional":
        return self + object

    def __add__(self, object: Union["Fractional", int, str]) -> "Fractional":
        object = self.check_type(object)
        self.common_denum(object)
        result_sum = Fractional(self._num + object._num, self._denum)
        self.slice()
        object.slice()
        return result_sum

    def __rsub__(self, object: Union["Fractional", int, str]) -> "Fractional":
        return self - object

    def __sub__(self, object: Union["Fractional", int, str]) -> "Fractional":
        object = self.check_type(object)
        object._sign *= -1
        result = self + object
        object._sign *= -1
        return result

    def __rtruediv__(self, object: Union["Fractional", int, str]) -> "Fractional":
        return self/object

    def __truediv__(self, object: Union["Fractional", int, str]) -> "Fractional":
        object = self.check_type(object)
        denum = self._denum * object._num
        num = self._num * object._denum
        return Fractional(num, denum)
    
    def __rmul__(self, object: Union["Fractional", int, str]) -> "Fractional":
        return self*object

    def __mul__(self, object: Union["Fractional", int, str]) -> "Fractional":
        object = self.check_type(object)
        num = self._sign * object._sign * self._num * object._num
        denum = self._denum * object._denum
        return Fractional(num, denum)

    def __iadd__(self, object: Union["Fractional", int, str]) -> "Fractional":
        object = self.check_type(object)
        return self + object

    def __isub__(self, object: Union["Fractional", int, str]) -> "Fractional":
        object = self.check_type(object)
        return self - object

    def __itruediv__(self, object: Union["Fractional", int, str]) -> "Fractional":
        object = self.check_type(object)
        return self / object

    def __imul__(self, object: Union["Fractional", int, str]) -> "Fractional":
        object = self.check_type(object)
        return self * object

    def __lt__(self, object: Union["Fractional", int, str]) -> bool:
        object = self.check_type(object)
        self.common_denum(object)
        if self._sign == -1 and object._sign == 1:
            return True
        if self._sign == 1 and object._sign == -1:
            return False
        if self._num < object._num:
            self.slice()
            object.slice()
            return True
        self.slice()
        object.slice()
        return False

    def __le__(self, object: Union["Fractional", int, str]) -> bool:
        object = self.check_type(object)
        if self < object or self == object:
            return True
        return False

    def __gt__(self, object: Union["Fractional", int, str]) -> bool:
        object = self.check_type(object)
        self.common_denum(object)
        if self._sign == -1 and object._sign == 1:
            return False
        if self._sign == 1 and object._sign == -1:
            return True
        if self._num > object._num:
            self.slice()
            object.slice()
            return True
        self.slice()
        object.slice()
        return False

    def __ge__(self, object: Union["Fractional", int, str]) -> bool:
        object = self.check_type(object)
        if self > object or self == object:
            return True
        return False

    def __ne__(self, object: Union["Fractional", int, str]) -> bool:
        object = self.check_type(object)
        return not self == object

    def __eq__(self, object: Union["Fractional", int, str]) -> bool:
        object = self.check_type(object)
        if self._sign != object._sign:
            return False
        if self._num != object._num:
            return False
        if self._denum != object._denum:
            return False
        return True

    def check_type(self, object) -> 'Fractional':
        if isinstance(object, Union[int, str]):
            object = Fractional(object)
        elif not isinstance(object,Fractional):
            raise TypeError(f"{type(object)} is not supported")
        return object

    def common_denum(self, object: "Fractional") -> bool:
        gcd = math.gcd(self._num, self._denum)
        if gcd == 1:
            self._num *= object._denum
            object._num *= self._denum
            self._denum *= object._denum
            object._denum = self._denum
            return
        if self._denum > object._denum:
            object._denum *= gcd
            object._num *= gcd
        else:
            self._denum *= gcd
            self._num *= gcd

    def slice(self) -> None:
        gcd = math.gcd(self._num, self._denum)
        if gcd != 1:
            self._num = int(self._num / gcd)
            self._denum = int(self._denum / gcd)

    @property
    def numerator(self) -> int:
        return self._num

    @numerator.setter
    def numerator(self, number: int) -> None:
        self._num = number
        self.slice()

    @property
    def denominator(self) -> int:
        return self._denum

    @denominator.setter
    def denominator(self, number: int) -> None:
        if number == 0:
            raise ValueError("Division by zero")
        self._denum = number
        self.slice()

def main():
    f = Fractional(3, -4)
    print(f)
    f = Fractional("3/9")
    print(f)
    a = Fractional(1, 2)
    b = Fractional(-1, 4)
    print(a + b, " sum")
    print(a - b, " sub")
    print(a * b, " mul")
    print(a / b, " div")
    a += b
    print(a, "sum")
    a = Fractional(1, 2)
    a -= b
    print(a, "sub")
    a = Fractional(1, 2)
    a *= b
    print(a, "mul")
    a = Fractional(1, 2)
    a /= b
    print(a, "div")
    a = Fractional(1, 2)
    b = Fractional(2, 4)
    print(a >= b)
    c = Fractional("3")
    print(c)
    print(c + '1')
    print("1" + c )
    print("3" / c)
    print("3" * c)
    f.denominator = 0

if __name__ =='__main__':
    main()