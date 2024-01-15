# 4
# Напишите функцию stairs, принимающую вектор и возвращающую матрицу,
# в которой каждая строка является копией вектора со смещением.

import numpy as np


def stairs(l):
    n = len(l)
    l = list(l)
    matrix = []
    for i in range(n):
        matrix.append(l[-i:] + l[:-i])
    return matrix

print(stairs(np.arange(5)))