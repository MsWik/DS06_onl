# Создайте случайный вектор размером 30 и найдите среднее значение
import numpy as np
a = np.random.randint(low=0, high=100, size = 30)

print(np.mean(a))