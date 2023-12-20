from scipy.stats import binom
import numpy as np

n = 100
k = 85
p = 0.8
q=1-p

# Вычисление вероятности с использованием биномиального распределения
probability = binom.pmf(k, n, p)
a = (p**k) * (q**(n-k)) * (np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n-k)))

print(f"Вероятность попадания в цель ровно 85 раз при 100 выстрелах (с использованием scipy): {probability:.4f}")
print(f"Вероятность попадания в цель ровно 85 раз при 100 выстрелах (вручную): {a:.4f}")


