# Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек.
# Какова вероятность, что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?

from scipy.stats import binom

p_failure = 0.0004
n_lamps = 5000
prob_no_failures = binom.pmf(0, n_lamps, p_failure)
prob_two_failures = binom.pmf(2, n_lamps, p_failure)
print(prob_no_failures, prob_two_failures)
