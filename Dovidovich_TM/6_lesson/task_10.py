from typing import List


def make_linear(list_values: List[any]) -> List[any]:
    while True:
        nothing_to_unpack = True
        for i in range(len(list_values)):
            if isinstance(list_values[i], List):
                nothing_to_unpack = False
                temp_sublist = list_values[i]
                del list_values[i]
                list_values.extend(temp_sublist)
        if nothing_to_unpack:
            return list_values


def task_10():
    result = make_linear([1, 2, [3, [4, 5]]])
    print(result)


if __name__ == '__main__':
    task_10()
