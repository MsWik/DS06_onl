# Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].
# Найдите ее среднее значение и дисперсию.

import numpy as np
from scipy import stats


a = np.arange(200,801)
a_mean = np.mean(a)
a_disp = np.var(a)
print(a_mean)
print(a_disp)