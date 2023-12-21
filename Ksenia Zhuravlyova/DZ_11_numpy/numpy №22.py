# Нормализовать матрицу случайных значений 5 на 5
import numpy as np
from sklearn. preprocessing import normalize

a = np.random.randint(low = 0, high=100, size=(5, 5))
a_normed = normalize(a, axis= 0 , norm='l1')
print(a_normed)
print('Проверим, что матрица "a" нормализованна по L1-норме: \n', np.sum(a_normed, axis=0)[:, np.newaxis])
