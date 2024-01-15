# # 1
# # Формат ввода Вводится последовательность рациональных чисел, разделённых пробелами.
# # Формат вывода Одно число — среднее геометрическое переданных чисел.

# # Ввод
# # 1 2 3 4 5

# # Вывод
# # 2.605171084697352


def geometric_mean():
    l = list(map(float, input().split()))
    answer = 1
    n = len(l)
    for elm in l:
        answer *= elm

    answer = answer ** (1 / n)
    print(answer)


if __name__ == "__main__":
    geometric_mean()