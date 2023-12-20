reverse_input=input("Введите числа через пробел:")
reverse_rezalt=reverse_input.split()
reverse_rezalt=reverse_rezalt[::-1]
reverse_rezalt= ' '.join(reverse_rezalt)
print (f"Ваш результат: {reverse_rezalt}")