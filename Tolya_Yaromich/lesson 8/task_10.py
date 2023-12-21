import numpy as np
import pandas as pd

def values(func, start, end, step):
    x_values = np.arange(start, end, step)
    y_values = [func(x) for x in x_values]
    data = pd.Series(y_values, index=x_values)
    return data

def min_extremum(data):
    min_value = data.min()
    min_index = data.idxmin()
    return min_index, min_value

def max_extremum(data):
    max_value = data.max()
    max_index = data.idxmax()
    return max_index, max_value

data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
min_point, min_value = min_extremum(data)
max_point, max_value = max_extremum(data)
print(f"Минимум: точка {min_point}, значение {min_value}")
print(f"Максимум: точка {max_point}, значение {max_value}")