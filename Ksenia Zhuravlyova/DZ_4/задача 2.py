#Ввод 12345 Вывод 5 (MAX)
n = input()
digits = [int(digit) for digit in n if digit == max(digit)]
print(max(digits))
