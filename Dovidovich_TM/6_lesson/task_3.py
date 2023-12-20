import numpy as np
from typing import Union


class Handler:
    def __init__(self, *args: Union[int, float]) -> None:
        self.__results = np.reshape(np.array([x for x in args]), (-1, 2))

    def __str__(self):
        return f'{self.__results}'

    def get_sum(self):
        return np.sum(self.__results, axis=0)

    def get_average(self):
        return np.mean(self.__results, axis=0)


def task_3():
    hand = Handler(1, 2, 3, 4)
    print(hand)
    print(hand.get_sum())
    print(hand.get_average())


if __name__ == '__main__':
    task_3()
