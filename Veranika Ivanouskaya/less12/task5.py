# Рост взрослого населения города X имеет нормальное распределение.
# Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.
# Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост: а). больше 182 см б). больше 190 см в).
# от 166 см до 190 см г). от 166 см до 182 см д). от 158 см до 190 см е). не выше 150 см или не ниже 190 см ё).
# не выше 150 см или не ниже 198 см ж). ниже 166 см.

from scipy.stats import norm

mean_height = 174
std_deviation = 8
prob_greater_than_182 = 1 - norm.cdf(182, mean_height, std_deviation)
prob_greater_than_190 = 1 - norm.cdf(190, mean_height, std_deviation)
prob_between_166_and_190 = norm.cdf(190, mean_height, std_deviation) - norm.cdf(166, mean_height, std_deviation)
prob_between_166_and_182 = norm.cdf(182, mean_height, std_deviation) - norm.cdf(166, mean_height, std_deviation)
prob_between_158_and_190 = norm.cdf(190, mean_height, std_deviation) - norm.cdf(158, mean_height, std_deviation)
prob_not_between_150_and_190 = norm.cdf(150, mean_height, std_deviation) + (1 - norm.cdf(190, mean_height, std_deviation))
prob_not_between_150_and_198 = norm.cdf(150, mean_height, std_deviation) + (1 - norm.cdf(198, mean_height, std_deviation))
prob_less_than_166 = norm.cdf(166, mean_height, std_deviation)

print(prob_greater_than_182, prob_greater_than_190, prob_between_166_and_190, prob_between_166_and_182, prob_between_158_and_190, prob_not_between_150_and_190, prob_not_between_150_and_198, prob_less_than_166)
