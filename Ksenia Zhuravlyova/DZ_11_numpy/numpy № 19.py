# Создайте матрицу 8x8 и залейте ее шахматным узором Пояснение к заданию:
# не используйте функцию tile. Ниже будет аналогичное задание 21 с использованием функции tile

import numpy as np

a = np.ones((8,8))

print(a)
a[1::2,::2] = 0
a[::2,1::2] = 0

print()
print(a)
#%%
