
'''Задача 1
Иногда требуется манипулировать с цифрами чисел. Одно из самых простых действий, которое можно совершить — найти сумму цифр числа.
Напишите программу, чтобы выполнить это действие.'''

number = input('Введите число: ')
digits = [int(digit) for digit in number]
sum_d = sum(digits)
print(sum_d)


'''Задача 2
Давайте попробуем выполнить ещё одно простое действие — найдём максимальную цифру числа.'''

max_d = max(digits)
print(max_d)

'''Задача 3
Мы уже достаточно знатоки, чтобы очистить число от определённых цифр, поэтому давайте напишем программу, которая уберёт все чётные цифры из числа.'''

number = input('Введите число: ')
digits = [int(digit) for digit in number]
odd_digits = [digit for digit in digits if digit % 2 != 0]
result = ''.join(map(str, odd_digits))
print(result)

'''Задача 4
Давайте сымитируем игру «Угадайка» между двумя людьми. Для этого нужно написать программу, которая отгадывает загаданное целое число от 1 до 1000 включительно. Пользователь (или тестирующая система) загадывает число и не сообщает его вашей программе. Угадать число нужно не более, чем за 10 попыток.

На каждую попытку пользователь отвечает одной из фраз:

Больше; Меньше; Угадал! Данная задача проверяется интерактивно. Другими словами, пока вы не выведите своё число, система не предоставит вам данных.'''


def ugadaika():
    lower_bound = 1
    upper_bound = 1000
    attempts = 0
    while True:
        guess = (lower_bound + upper_bound) // 2
        attempts += 1
        response = input(f"Попытка {attempts}: Это число {guess}? : ")
        if response == "Угадал!":
            print(f"Угадано за {attempts} попыток!")
            break
        elif response == "Больше":
            lower_bound = guess + 1
        elif response == "Меньше":
            upper_bound = guess - 1
        else:
            print("Некорректный ответ. Пожалуйста, введите 'Больше', 'Меньше' или 'Угадал!'.")


ugadaika()


'''Задача 5
Файловая статистика
Напишите программу, которая для заданного файла вычисляет следующие параметры:
количество всех чисел;
количество положительных чисел;
минимальное число;
максимальное число;
сумма всех чисел;
среднее арифметическое всех чисел с точностью до двух знаков после запятой.
Формат вывода Выведите статистику в указанном порядке.'''


def analise_of_file():
    file_path = input("Введите имя файла: ")
    with open(file_path, "r") as file:
        content = file.read()
    numbers = [float(num) for num in content.split()]
    total_numbers = len(numbers)
    positive_numbers = len([num for num in numbers if num > 0])
    min_number = min(numbers)
    max_number = max(numbers)
    sum_of_numbers = sum(numbers)
    average = sum_of_numbers / total_numbers

    print("Количество всех чисел:", total_numbers)
    print("Количество положительных чисел:", positive_numbers)
    print("Минимальное число:", min_number)
    print("Максимальное число:", max_number)
    print("Сумма всех чисел:", sum_of_numbers)
    print("Среднее арифметическое всех чисел:", round(average, 2))


analise_of_file()

'''Задача 6
По пути домой родители вновь решили сыграть с детьми в поиск зверушек.
Формат ввода Три строки описывающих придорожную местность.
Формат вывода Строка в которой есть зайка, а затем её длина. Если таких строк несколько, выбрать ту, что меньше всех лексикографически.'''


def where_is_zayka():
    input_text = input("Введите описание придорожной местности: ")
    input_list = input_text.split()
    zayka = None

    for i in range(len(input_list)):
        if "зайка" in input_list[i]:
            zayka = " ".join(input_list[:i + 1])
            break

    if zayka:
        print(f"{zayka} {len(zayka)}")
    else:
        print("Зайка не найдена")


where_is_zayka()


'''Задача 7
Вспомним, что простые числа — те натуральные числа, у которых два делителя: оно само и 1. Напишите программу для определения количества простых чисел среди введённых..'''


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input())
count = 0
for i in range(n):
    x = int(input())
    if is_prime(x):
        count += 1

print(count)





