# По пути домой родители вновь решили сыграть с детьми в поиск зверушек.
# Формат ввода Три строки описывающих придорожную местность.
# Формат вывода Строка в которой есть зайка, а затем её длина. Если таких строк несколько, выбрать ту, что меньше всех лексикографически.
# Пример
# Ввод
# березка елочка зайка волк березка
# сосна сосна сосна елочка грибочки медведь
# сосна сосна сосна белочка сосна белочка
# Вывод
# березка елочка зайка волк березка 33


def task_1():
    number = 3
    strings = []
    for _ in range(number):
        string = input()
        if "зайка" in string:
            strings.append(string)
    print(strings[0], len(strings[0])) if len(strings) == 1 else print(
        min(strings, key=len), len(min(strings, key=len))
    )


if __name__ == "__main__":
    task_1()
