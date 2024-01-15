# #2
# Давайте попробуем выполнить ещё одно простое действие — найдём максимальную цифру числа.

# Пример
# Ввод 12345 Вывод 5

def max_digit():
    n = input()
    print(max([int(digit) for digit in n]))

if __name__ == "__main__":
    max_digit()