# #3
# Мы уже достаточно знатоки, чтобы очистить число от определённых цифр,
# поэтому давайте напишем программу, которая уберёт все чётные цифры из числа.

# Пример
# Ввод 1234 Вывод 13

def without_even():
    n = input()
    print(''.join(filter(lambda x: int(x) % 2 != 0, n)))

if __name__ == "__main__":
    without_even()