#Ввод 1234 Вывод 13 убрать все четные числа
input_string = input("Введите строку из цифр: ")
filtered_digits = ''.join(filter(lambda digit: int(digit) % 2 != 0, input_string))
print(filtered_digits)
