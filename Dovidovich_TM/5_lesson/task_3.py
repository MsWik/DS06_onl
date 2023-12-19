# Мы уже достаточно знатоки, чтобы очистить число от определённых цифр,
# поэтому давайте напишем программу, которая уберёт все чётные цифры из числа.
# Пример
# Ввод 1234 Вывод 13


def task_3():
    numbers = list(input())
    numbers = [number for number in numbers if int(number) % 2 == 1]
    print("".join(numbers))


if __name__ == "__main__":
    task_3()
