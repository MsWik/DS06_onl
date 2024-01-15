# Задача 3

# Лаборанты проводят эксперимент и запросили разработку системы обработки данных.
# Результатами эксперимента должны стать пары рациональных чисел.
# Для работы им требуются функции:
# enter_results(first, second, ...) — добавление данных одного или нескольких результатов
# (гарантируется, что количество параметров будет чётным);
# get_sum() — возвращает пару сумм результатов экспериментов;
# get_average() — возвращает пару средних арифметических значений результатов экспериментов.

result_1 = []
result_2 = []

def enter_results(*args):
    global result_1
    global result_2
    result_1 += args[::2]
    result_2 += args[1::2]

def get_sum():
    return sum(result_1), sum(result_2)

def get_average():
    return sum(result_1) / len(result_1), sum(result_2) / len(result_2)

if __name__ == "__main__":
    enter_results(1,2,3,4,5,6)
    print(get_sum())
    print(get_average())

    enter_results(1,1)
    print(get_sum())
    print(get_average())