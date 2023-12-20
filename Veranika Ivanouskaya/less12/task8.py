# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

from scipy.stats import binom

p_hit = 0.8
n_shots = 100
k_hits = 85
prob_85_hits = binom.pmf(k_hits, n_shots, p_hit)

print(prob_85_hits)
