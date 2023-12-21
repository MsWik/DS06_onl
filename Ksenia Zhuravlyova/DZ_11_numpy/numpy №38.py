# Рассмотрим функцию генератора, которая генерирует 10 целых чисел и использует ее для построения массива.


import numpy as np

# Определение функции генератора
def generate_numbers():
    for _ in range(10):
        yield np.random.randint(1, 100)

# Создание массива с использованием функции генератора
generated_array = np.fromiter(generate_numbers(), dtype=int)

# Вывод результата
print("Сгенерированный массив:", generated_array)
