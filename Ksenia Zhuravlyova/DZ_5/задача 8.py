# Напишите рекурсивную функцию merge_sort, которая производит сортировку списка.

def merge_twolist(list_a: List[int], list_b: List[int]) -> List[int]):

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

def merge_sort():
    return sorted(merge_twolist)