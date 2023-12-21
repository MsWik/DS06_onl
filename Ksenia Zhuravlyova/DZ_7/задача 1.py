# Формат ввода Вводится последовательность рациональных чисел, разделённых пробелами.
# Формат вывода Одно число — среднее геометрическое переданных чисел.
# Ввод
# 1 2 3 4 5
# Вывод
# 2.605171084697352


import math

def calculate_geometric_mean(numbers):
    if len(numbers) == 0:
        return None

    product = 1
    for num in numbers:
        product *= num

    geometric_mean = math.pow(product, 1/len(numbers))
    return geometric_mean

# Считываем последовательность чисел и преобразуем их в числа с плавающей запятой
input_str = input()
numbers = [float(x) for x in input_str.split()]

result = calculate_geometric_mean(numbers)

if result is not None:
    print(result)
else:
    print("Пустой ввод.")






