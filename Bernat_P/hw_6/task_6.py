def merge(list_a: list[int], list_b: list[int]) -> list[int]:
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


def merge_sort(obj: list[int]):
  if len(obj) <= 1:
    return obj
  else:

    mid = len(obj) // 2
    right_obj = obj[:mid]
    left_obj = obj[mid:]

    right_sort = merge_sort(right_obj)
    left_sort = merge_sort(left_obj)

    return  merge(right_sort, left_sort)


if __name__ == '__main__':
  print(merge_sort([134,4,1,8,3,81]))

