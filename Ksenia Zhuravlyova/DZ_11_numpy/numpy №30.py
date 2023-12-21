# Как найти общие значения между двумя массивами

import numpy as np

a = np.random.randint(0, 10, 10)
b = np.random.randint(0, 10, 10)

ab = np.intersect1d(a, b)
print(a)
print(b)
print(ab)