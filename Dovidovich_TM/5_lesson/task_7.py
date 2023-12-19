# Вспомним, что простые числа — те натуральные числа, у которых два делителя: оно само и 1.
# Напишите программу для определения количества простых чисел среди введённых.
# Формат ввода В первой строке записано число N Во всех последующих N строках — по одному числу.
# Формат вывода Требуется вывести общее количество простых чисел среди введённых (кроме N).
# Ввод
# 5
# 1
# 2
# 3
# 4
# 5
# Вывод
# 3


def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def task_7():
    N = int(input())
    number_of_primes = 0
    for _ in range(N):
        if is_prime(int(input())):
            number_of_primes += 1
    print(number_of_primes)


if __name__ == "__main__":
    task_7()
