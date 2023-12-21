# Создайте двумерный-массив с 1(единицами) на границе и 0(нулями) внутри

import numpy as np
a = np.ones((5,5))
print(a)
print()
a[1:-1,1:-1] = 0
print(a)