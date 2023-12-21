# Напишите функцию multiplication_matrix, которая принимает размер матрицы (N)
# и возвращает массив описывающий таблицу умножения N на N.
#print(multiplication_matrix(3))
# Вывод
# [[1 2 3]
#  [2 4 6]
#  [3 6 9]]

import numpy as np

def multiplication_matrix(n):
    # Создаем пустую матрицу размером n x n, заполненную нулями
    matrix = np.zeros((n, n), dtype=int)

    # Заполняем матрицу значениями
    for i in range(n):
        for j in range(n):
            matrix[i][j] = (i + 1) * (j + 1)

    return matrix

# Вызываем функцию и выводим результат
result = multiplication_matrix(3)
print(result)