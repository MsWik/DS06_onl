import scipy.stats as stats

# Заданные параметры распределения
mean_height = 174  # средний рост
std_deviation = 8  # среднее квадратичное отклонение

# Диапазоны роста
height_ranges = [
    (182, float('inf')),      # Больше 182 см
    (190, float('inf')),      # Больше 190 см
    (166, 190),               # От 166 см до 190 см
    (166, 182),               # От 166 см до 182 см
    (158, 190),               # От 158 см до 190 см
    (-float('inf'), 150),     # Не выше 150 см
    (198, float('inf')),      # Не ниже 198 см
    (-float('inf'), 166)      # Ниже 166 см
]

# Вероятности для каждого диапазона
for height_range in height_ranges:
    z_lower = (height_range[0] - mean_height) / std_deviation
    z_upper = (height_range[1] - mean_height) / std_deviation

    probability = stats.norm.cdf(z_upper) - stats.norm.cdf(z_lower)

    print(f"Вероятность для диапазона {height_range}: {probability:.4f}")