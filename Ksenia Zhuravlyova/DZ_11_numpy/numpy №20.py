# Рассмотрим массив формы (6,7,8), каков индекс (x, y, z) 100-го элемента?

import numpy as np

shape = (6, 7, 8)
linear_index = 100
indices = np.unravel_index(linear_index, shape)
print(indices)
