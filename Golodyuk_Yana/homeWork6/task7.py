# Задача 7

# Напишите рекурсивную функцию merge_sort, которая производит сортировку списка.

from typing import List


def merge(list_a: List[int], list_b: List[int]) -> List[int]:
    answer = []
    i = 0
    j = 0
    n = len(list_a)
    m = len(list_b)
    while i != n and j != m:
        if list_a[i] < list_b[j]:
            answer.append(list_a[i])
            i += 1
        else:
            answer.append(list_b[j])
            j += 1
    if i == n:
        answer += list_b[j:]
    else:
        answer += list_a[i:]
    return answer


def merge_sort(l):
    n = len(l)

    if n == 1 or n == 0:
        return l

    return merge(merge_sort(l[: n // 2]), merge_sort(l[n // 2 :]))


if __name__ == "__main__":
    print(merge_sort([5, 4, 3, 2, 1, -1]))