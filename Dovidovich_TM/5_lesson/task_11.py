# Формат ввода Вводится 3 вещественных числа
# a,b,c
# — коэффициенты уравнения вида:
# ax2+bx+c=0
# Формат вывода
# Если у уравнения нет решений — следует вывести «No solution».
# Если корней конечное число — их нужно вывести через пробел в порядке возрастания с точностью до сотых.
# Если корней неограниченное число — следует вывести «Infinite solutions».
# Примечание
# Обратите внимание, что ограничения на значения коэффициентов отсутствуют.
# Пример 1
# Ввод: 1 -2 1
# Вывод: 1.00


def existing(number_a, number_b, number_d):
    if number_d < 0:
        print("No solution")
        return False
    elif number_a == number_b == 0:
        print("Infinite solutions")
        return False
    elif number_d == 0:
        print("{:.2f}".format(-number_b / (2 * number_a)))
        return False
    return True


def task_11():
    number_a, number_b, number_c = map(int, input().split())
    number_d = number_b**2 - 4 * (number_a * number_c)
    if existing(number_a, number_b, number_d) == False:
        return

    solutions = []
    solutions.append((pow(number_d, 1 / 2) - number_b) / (2 * number_a))
    solutions.append(-number_b / solutions[0])
    solutions.sort()
    for x in solutions:
        print("{:.2f}".format(x))


if __name__ == "__main__":
    task_11()
