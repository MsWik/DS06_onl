import numpy as np
mas = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask = (mas >= 3) & (mas <= 8)
mas[mask] *= -1
print(mas)

i=np.array(0) / np.array(0)
print(i)

j=np.array(0) // np.array(0)
print(j)
x=np.array([np.nan]).astype(int).astype(float)
print(x)