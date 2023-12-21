def zayka():
    n = int(input("Введите количество строк: "))
    word = 'зайка'
    min_line = None

    for _ in range(n):
        line = input("Введите строку: ")
        if word in line:
            if min_line is None or len(line) < len(min_line):
                min_line = line

    if min_line is not None:
        print(min_line, len(min_line))
    else:
        print("Нет строк с словом 'зайка'")

zayka()