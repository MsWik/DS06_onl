def merge(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c

def merge_sort(sorter):
    if len(sorter) <= 1:
        return sorter
    middle = len(sorter) // 2
    left = merge_sort(sorter[:middle])
    right = merge_sort(sorter[middle:])
    return merge(left, right)

print(merge_sort([7, 5, 2, 3, 9, 4]))
