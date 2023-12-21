# Создайте матрицу шахматной доски 8x8, используя функцию tile

import numpy as np
a = np.array([[1, 0], [0, 1]])
print(a)
print()
a = np.tile(a,(4,4))
print(a)
