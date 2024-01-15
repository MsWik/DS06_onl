# #5

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


from functools import reduce

def calc_params():
    numbers = []
    with open('numbers.txt') as f:
        lines = f.readlines()
        for line in lines:
            numbers += line.split()
        numbers = list(map(int, numbers))

    print(len(numbers), len(list(filter(lambda x: x > 0, numbers))), min(numbers), max(numbers), sum(numbers), round(sum(numbers) / len(numbers), 2))

if __name__ == "__main__":
    calc_params()