import numpy as np

# Заданные значения зарплат
zarplata = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

# Среднее арифметическое
average = np.sum(zarplata) / len(zarplata)

# Среднее квадратичное отклонение 
Sum_kv_otkl = np.sum((zarplata - average) ** 2)
awerage_quadro_otkl = np.sqrt(Sum_kv_otkl / len(zarplata))

# Смещенная оценка дисперсии
dispersion = Sum_kv_otkl / len(zarplata)

# Несмещенная оценка дисперсии
dispersion_2 = Sum_kv_otkl / (len(zarplata) - 1)

print(f"Среднее арифметическое: {average}")
print(f"Среднее квадратичное отклонение: {awerage_quadro_otkl}")
print(f"Смещенная оценка дисперсии: {dispersion}")
print(f"Несмещенная оценка дисперсии: {dispersion_2}")




# Среднее арифметическое
average = np.mean(zarplata)

# Среднее квадратичное отклонение
awerage_quadro_otkl = np.std(zarplata, ddof=0)  

# Смещенная оценка дисперсии
dispersion = np.var(zarplata, ddof=0)

# Несмещенная оценка дисперсии
dispersion_2 = np.var(zarplata, ddof=1)

print(f"Среднее арифметическое: {average}")
print(f"Среднее квадратичное отклонение: {awerage_quadro_otkl}")
print(f"Смещенная оценка дисперсии: {dispersion}")
print(f"Несмещенная оценка дисперсии: {dispersion_2}")