def counter():
    n = int(input())
    word = 'зайка'
    c = 0           # количество заек
    for _ in range (n):
        s = input()
        for word in s.split():
            c += word.count('зайка')

    print(c)