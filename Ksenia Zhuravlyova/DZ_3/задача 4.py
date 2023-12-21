from itertools import groupby

numbers = input()  # Ввод строки с числами

# Группируем последовательности одинаковых чисел
groups = [(k, list(g)) for k, g in groupby(numbers)]

for key, group in groups:
    # Выводим само число и количество повторений
    print(key, len(group))

