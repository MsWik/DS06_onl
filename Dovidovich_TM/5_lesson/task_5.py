# Файловая статистика
# Напишите программу, которая для заданного файла вычисляет следующие параметры:
# количество всех чисел;
# количество положительных чисел;
# минимальное число;
# максимальное число;
# сумма всех чисел;
# среднее арифметическое всех чисел с точностью до двух знаков после запятой.
# Формат ввода
# Пользователь вводит имя файла.
# Файл содержит произвольное количество чисел, разделённых пробелами и символами перевода строки.
# Формат вывода Выведите статистику в указанном порядке.
# Ввод
# numbers.txt
# Содержимое файла numbers.txt
# 1 2 3 4 5
# -5 -4 -3 -2 -1
# 10 20
# 20 10
# Вывод
# 14
# 9
# -5
# 20
# 60
# 4.29
import numpy as np


def data_normalization(file_name: str):
    data = []
    with open("numbers.txt", "r") as input_file:
        for line in input_file:
            data.append((line.strip("\n")))
    data = [int(number) for numbers in data for number in numbers.split()]
    input_file.close()
    return data


def data_analysis(data):
    # numbers
    print(len(data))
    # numbers of postitive
    numbers_positive = 0
    for number in data:
        if number > 0:
            numbers_positive += 1
    print(numbers_positive)
    # min
    print(min(data))
    # max
    print(max(data))
    # sum
    print(sum(data))
    # mean
    print("{:.2f}".format(np.mean(np.array(data))))


def task_5():
    file_name = "numbers_txt"
    data = data_normalization(file_name)
    data_analysis(data)


if __name__ == "__main__":
    task_5()
