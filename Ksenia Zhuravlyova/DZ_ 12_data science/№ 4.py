# Непрерывная случайная величина X распределена нормально и задана плотностью распределения
# f(x) = (1 / (4_ sqrt(2pi)))_exp((-(x+2)**2) / 32) Найдите:
# а). M(X)
# б). D(X)
# в). std(X) (среднее квадратичное отклонение)


import numpy as np

# Заданные параметры
mu = -2
sigma = 4
#f(x) = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))

M_x = mu
D_x = np.sqrt(sigma)
std_x = sigma


# Вывод результатов
print("a) M(X) =", M_x)
print("б) D(X) =", D_x)
print("в) std(X) =", std_x)


