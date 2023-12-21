# Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

salaries = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
mean_salary = sum(salaries) / len(salaries)
squared_diffs = [(salary - mean_salary) ** 2 for salary in salaries]
biased_variance = sum(squared_diffs) / len(salaries)
unbiased_variance = sum(squared_diffs) / (len(salaries) - 1)
std_deviation = (biased_variance) ** 0.5
print(mean_salary, std_deviation, biased_variance, unbiased_variance)
