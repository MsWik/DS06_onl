# 10
# Напишите три функции:
# values(func, start, end, step), строящую Series значений функции в точках диапазона и принимающую:

# функцию одной переменной;
# начало диапазона;
# конец диапазона;
# шаг вычисления;

# min_extremum(data) возвращает точку, в которой был достигнут минимум на диапазоне;
# max_extremum(data) возвращает точку, в который был достигнут максимум на диапазоне.

import pandas as pd

def values(func, start, end, step):
    x_ = []
    y_ = []
    while start <= end + 10e-6:
        x_.append(start)
        y_.append(func(start))
        start += step
    return pd.Series(y_, index=x_)


def min_extremum(data: pd.Series):
    return (data[data == data.min()]).index[0]


def max_extremum(data: pd.Series):
    return (data[data == data.max()]).index[0]


data = values(lambda x: x**2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))
