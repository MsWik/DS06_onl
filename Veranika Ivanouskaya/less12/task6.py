# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

from scipy.stats import binom

n = 144
k = 70
p = 0.5

probability = binom.pmf(k, n, p)
print(probability)
