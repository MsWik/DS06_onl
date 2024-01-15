# #8
# Напишите программу, которая строит числовой прямоугольник требуемого размера.

# Формат ввода В первой строке записано число N — высота числового прямоугольника.
# Во второй строке указано число M — ширина числового прямоугольника.

# Формат вывода
# Нужно вывести сформированный числовой прямоугольник требуемого размера.
# Чтобы прямоугольник был красивым, каждый его столбец должен обладать одинаковой шириной.

from typing import List
numbers = []

def build_rectangle() -> object:
    N = int(input())
    M = int(input())

    global numbers
    numbers = [[i + 1 + j * N for j in range(M)] for i in range(N)]
    return numbers


def print_matrix(numbers: List[int]):
    for row in numbers:
        for element in row:
            print(element, end=" ")
        print()


if __name__ == "__main__":
    build_rectangle()
    print_matrix(numbers)