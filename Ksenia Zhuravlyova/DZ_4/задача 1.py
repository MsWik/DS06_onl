#Ввод 12345 Вывод 15

n = input()  # Ввод строки
digits = [int(digit) for digit in n]  # Преобразуем строку в список цифр

s = sum(digits)  # Суммируем цифры в списке

print("Сумма цифр:", s)