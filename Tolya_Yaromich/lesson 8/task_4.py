import numpy as np
def stairs():
    j=0
    index = int(input("Введите число: "))
    rows = []
    for i in range(index):
        row = np.arange(index)
        rows.append(row)
    matrix = np.array(rows)
    for i in range(index):
        matrix[i] = np.roll(matrix[i], shift=j, axis=0)
        j+=1
    print(matrix)
stairs()