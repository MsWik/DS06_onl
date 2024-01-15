# Задача 4

# RLE означает “run-length encoding”. 
# Это способ сокращённой записи последовательности чего угодно (в случае этой задачи — цифр). 
# При нём для подряд идущей группы одинаковых цифр (run) 
# записываются сама эта цифра и длина этой группы (run length). 
# Таким образом, 99999 превратится в 9 5 («девять пять раз») и так далее. 
# RLE широко используется в самых разных областях. 
# Напишите программу, которая кодирует строку цифр в RLE.
# Формат ввода Строка цифр длиной не меньше 1.
# Формат вывода Пары: сама цифра и количество повторений цифры подряд во введённой строке, 
# как описано в условии и показано в примере.
# Ввод
# 010000100001111111110111110000000000000011111111
# Вывод
# 0 1
# 1 1
# 0 4
# 1 1
# 0 4
# 1 9
# 0 1
# 1 5
# 0 14
# 1 8

def foo():
    num = input()
    target = num[0]
    cnt = 0 
    for element in num:
        if target == element:
            cnt += 1
        else:
            print(target, cnt)
            target = element
            cnt = 1
    print(target, cnt)

if __name__ == ("__main__"):
    foo()