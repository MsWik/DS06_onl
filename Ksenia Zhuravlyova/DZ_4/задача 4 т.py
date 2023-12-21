def suprize():
    user_number = int(input())  # число пользователя
    guess_number = 500  # начинаем с середины интервала [1, 1000]
    attempts = 0  # число попыток пользователя

    while attempts < 10:
        response = input(f"Попытка {attempts + 1}: {guess_number} - Меньше, Больше или Угадал? ")

        if response == "Угадал":
            print(f"Поздравляем! Вам понадобилось {attempts} попыток, чтобы угадать число {user_number}.")
            return
        elif response == "Меньше":
            guess_number = (guess_number + 1 + user_number) // 2  # Изменяем верхнюю границу интервала
        elif response == "Больше":
            guess_number = (guess_number + 1000) // 2  # Изменяем нижнюю границу интервала
        else:
            print("Пожалуйста, введите одно из следующих слов: Меньше, Больше или Угадал.")

        attempts += 1

    print("Игра окончена. Вам не удалось угадать число.")