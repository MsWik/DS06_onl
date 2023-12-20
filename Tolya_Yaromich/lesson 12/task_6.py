from scipy.stats import binom
import numpy as np
n = 144
k = 70
p = 0.5
q=1-p
# Вычисление вероятности с использованием биномиального распределения
probability = binom.pmf(k, n, p)
a = (p**k) * (q**(n-k)) * (np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k)))

print(f"Вероятность выпадения орла ровно 70 раз в 144 бросках (с использованием scipy): {probability:.4f}")
print(f"Вероятность выпадения орла ровно 70 раз в 144 бросках (вручную): {a:.4f}")

