# Напишите функцию stairs, принимающую вектор и возвращающую матрицу,
# в которой каждая строка является копией вектора со смещением.

#print(stairs(np.arange(5)))
# Вывод
# [[0 1 2 3 4]
#  [4 0 1 2 3]
#  [3 4 0 1 2]
#  [2 3 4 0 1]
#  [1 2 3 4 0]]

import numpy as np

def stairs(vector):
    n = len(vector)
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        matrix[i] = np.roll(vector, i)
    return matrix

result = stairs(np.arange(5))
print(result)
