# О случайной непрерывной равномерно распределенной величине B известно,
# что ее дисперсия равна 0.2. Можно ли найти правую границу величины B и ее среднее значение зная,
# что левая граница равна 0.5? Если да, найдите ее.

import numpy as np
from scipy import stats

# Известные значения
a = 0.5
b_var = 0.2

# Находим правую границу (b) из уравнения дисперсии
b = np.sqrt(12 * b_var) + a

mu = (a + b) / 2

print(mu)


