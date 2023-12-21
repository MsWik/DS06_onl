# Как суммировать небольшой массив быстрее, чем np.sum

import numpy as np

vec = np.random.randint(0,100, 10)
print(vec)

print(np.add.reduce(vec))


