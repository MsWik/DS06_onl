import numpy as np
a = 0.5


dispersion =0.2

b = np.abs(dispersion **12)+a
average = (a + b) / 2


print(f"Среднее значение: {average}")
print(f"Дисперсия: {dispersion}")