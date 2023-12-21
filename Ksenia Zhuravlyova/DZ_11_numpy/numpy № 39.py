# Создайте вектор размера 10 со значениями от 0 до 1, за исключением границ отрезка 0 и 1

import numpy as np

vec = np.linspace(0, 1, 12, endpoint=False)[1:-1]

print(vec)