from typing import List, Tuple, Union


def make_matrix(size: Union[int, Tuple[int, int]], value: Union[int, float] = 0) -> List[List[int]]:
    if isinstance(size, int):
        matrix = [[value for i in range(size)]for j in range(size)]
    else:
        matrix = [[value for i in range(size[1])]for j in range(size[0])]
    return matrix


def task_2():
    size = (3, 4)
    print(make_matrix(size, 1))


if __name__ == '__main__':
    task_2()
