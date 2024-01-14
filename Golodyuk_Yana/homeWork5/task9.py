# 9
# Палиндром. Количество палиндромов в списке

# Ввод
# 3
# 123
# 454
# 321

# Вывод
# 1


def count_polidrom(n: int):
    cnt = 0
    for i in range(n):
        t = input()
        if t == t[::-1]:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    count_polidrom(5)

# Вариант Олега

# def is_polindrom(s):
#     return int(s == s[::-1])

# def count_polindrom():
#     answer = 0
#     N = int(input())
#     while N:
#         N -= 1
#         answer += is_polindrom(input())
#     print(answer)

# if __name__ == "__main__":
#     count_polindrom()
