import numpy as np
from scipy.stats import norm


average_height = 174
std_deviation = 8


вероятность_а = 1 - norm.cdf(182, loc=average_height, scale=std_deviation)


вероятность_б = 1 - norm.cdf(190, loc=average_height, scale=std_deviation)


вероятность_в = norm.cdf(190, loc=average_height, scale=std_deviation) - norm.cdf(166, loc=average_height, scale=std_deviation)


вероятность_г = norm.cdf(182, loc=average_height, scale=std_deviation) - norm.cdf(166, loc=average_height, scale=std_deviation)

вероятность_д = norm.cdf(190, loc=average_height, scale=std_deviation) - norm.cdf(158, loc=average_height, scale=std_deviation)


вероятность_е = norm.cdf(150, loc=average_height, scale=std_deviation) + (1 - norm.cdf(190, loc=average_height, scale=std_deviation))

вероятность_ё = norm.cdf(150, loc=average_height, scale=std_deviation) + (1 - norm.cdf(198, loc=average_height, scale=std_deviation))


вероятность_ж = norm.cdf(166, loc=average_height, scale=std_deviation)


print(f"а) Вероятность больше 182 см: {вероятность_а:.4f}")
print(f"б) Вероятность больше 190 см: {вероятность_б:.4f}")
print(f"в) Вероятность от 166 см до 190 см: {вероятность_в:.4f}")
print(f"г) Вероятность от 166 см до 182 см: {вероятность_г:.4f}")
print(f"д) Вероятность от 158 см до 190 см: {вероятность_д:.4f}")
print(f"е) Вероятность не выше 150 см или не ниже 190 см: {вероятность_е:.4f}")
print(f"ё) Вероятность не выше 150 см или не ниже 198 см: {вероятность_ё:.4f}")
print(f"ж) Вероятность ниже 166 см: {вероятность_ж:.4f}")