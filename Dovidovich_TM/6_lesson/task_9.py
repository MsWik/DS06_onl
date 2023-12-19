from typing import List


def cycle(list_values: List[any]) -> any:
    while True:
        for item in list_values:
            yield item


def task_9():
    print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))


if __name__ == '__main__':
    task_9()
