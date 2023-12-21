# Создайте матрицу 5x5 со значениями строк от 0 до 4

import numpy as np
a = np.arange(5)
matrix = np.tile(a, (5,1))
print(a)
print()
print(matrix)