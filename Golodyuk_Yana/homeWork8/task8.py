# 8
# Напишите три функции:
# values(func, start, end, step), строящую Series значений функции в точках диапазона и принимающую:
# функцию одной переменной;
# начало диапазона;
# конец диапазона;
# шаг вычисления;
# min_extremum(data) возвращает точку, в которой был достигнут минимум на диапазоне;
# max_extremum(data) возвращает точку, в который был достигнут максимум на диапазоне.


import pandas as pd


def need_to_work_better(data: pd.DataFrame):
    return data[(data == 2).any(axis=1)]


columns = ["name", "maths", "physics", "computer science"]
data = {
    "name": ["Иванов", "Петров", "Сидоров", "Васечкин", "Николаев"],
    "maths": [5, 4, 5, 2, 4],
    "physics": [4, 4, 4, 5, 5],
    "computer science": [5, 2, 5, 4, 3],
}
journal = pd.DataFrame(data, columns=columns)
filtered = need_to_work_better(journal)
print(journal)
print(filtered)
