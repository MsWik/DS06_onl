# Давайте сымитируем игру «Угадайка» между двумя людьми.
# Для этого нужно написать программу, которая отгадывает загаданное целое число от 1 до 1000 включительно.
# Пользователь (или тестирующая система) загадывает число и не сообщает его вашей программе.
# Угадать число нужно не более, чем за 10 попыток.
# На каждую попытку пользователь отвечает одной из фраз:
# Больше; Меньше; Угадал! Данная задача проверяется интерактивно. Другими словами, пока вы не выведите своё число, система не предоставит вам данных.
from random import randint


def number_selection(a, b, numbers):
    while True:  # Система выбирает число и проверяет пробовала ли она его уже
        number = randint(a, b)
        if number not in numbers:
            print(number)
            numbers.append(number)
            break


def task_4():
    target_number = int(input("Загадайте число: "))
    numbers = []
    attempt = 0
    a, b = 1, 1000  # ренджа
    while attempt < 10:
        attempt += 1
        number = number_selection(a, b, numbers)
        user_response = input().lower()
        match user_response:
            case "меньше":
                b = number - 1
            case "больше":
                a = number + 1
            case "угадал!":
                break
    else:
        print("Система проиграла.")


if __name__ == "__main__":
    task_4()
