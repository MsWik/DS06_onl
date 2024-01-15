# Всё в том же детском саду ребята очень любят играть с цифрами.
# Одна из таких игр — перестановка цифр четырёхзначного числа.
# Напишите программу для робота-няни, которая из числа вида abcd составляет число badc.
# Пример:
# Ввод
# 1234
# Вывод 2143


# Вариант 1
def func():
    num = input()
    print(num[1], num[0], num[3], num[2], sep="")


if __name__ == "__main__":
    func()


# # Вариант 2
# def func():
#     num = list(input())
#     num[::2], num[1::2] = num [1::2], num[::2]
#     num_str = "".join(num)
#     print(num_str)

# if __name__ == "__main__":
#     func()

# # Вариант 3
# def func():
#     a, b, c, d = input()
#     print(b, a, d, c, sep="")

# if __name__ == "__main__":
#     func()
