# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

import math

def binomial_probability(n, k, p):
    # Вычисление биномиального коэффициента C(n, k)
    binomial_coefficient = math.comb(n, k)

    # Вычисление вероятности по формуле биномиального распределения
    probability = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))

    return probability

# Параметры задачи
n_total_trials = 144
k_successes = 70
p_success = 0.5  # Вероятность выпадения орла в одном испытании

# Вычисление вероятности
probability_result = binomial_probability(n_total_trials, k_successes, p_success)
print(f"Вероятность, что орел выпадет ровно 70 раз: {probability_result:.4f}")



