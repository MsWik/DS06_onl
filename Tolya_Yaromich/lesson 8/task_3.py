import numpy as np

N=int(input("Введите N: "))
def multiplication_matrix(N):
    result = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            result[i, j] = (i + 1) * (j + 1)

    return result

matrix = multiplication_matrix(N)
print(matrix)