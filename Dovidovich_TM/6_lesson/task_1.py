from typing import Tuple


def tuple_sum(tuple_1: Tuple[int, int], tuple_2: Tuple[int, int]) -> Tuple[int, int]:
    return tuple([tuple_1[0]+tuple_2[0], tuple_1[1]+tuple_2[1]])


def can_eat(coordinates_horse: Tuple[int, int], coordinates_figure: Tuple[int, int]) -> bool:
    for move in [(2, 1), (-2, 1), (2, -1), (-2, -1)]:
        if tuple_sum(coordinates_horse, move) == coordinates_figure:
            return True
    return False


def task_1():
    print(can_eat((0, 0), (-2, 1)))


if __name__ == '__main__':
    task_1()
