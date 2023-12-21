#Лаборанты проводят эксперимент и запросили разработку системы обработки данных.
# Результатами эксперимента должны стать пары рациональных чисел.
# Для работы им требуются функции:
# enter_results(first, second, ...) — добавление данных одного или нескольких результатов
# (гарантируется, что количество параметров будет чётным);
# get_sum() — возвращает пару сумм результатов экспериментов;
# get_average() — возвращает пару средних арифметических значений результатов экспериментов.

def enter_results(results, *args):
    if len(args) % 2 != 0:
        raise ValueError("Количество параметров должно быть четным")
    results.extend(args)

def get_sum(results):
    if not results:
        return (0, 0)
    sum_first = sum(results[::2])
    sum_second = sum(results[1::2])
    return (sum_first, sum_second)

def get_average(results):
    if not results:
        return (0, 0)
    avg_first = sum(results[::2]) / len(results[::2])
    avg_second = sum(results[1::2]) / len(results[1::2])
    return (avg_first, avg_second)

# Пример использования:
results = []
enter_results(results, 1, 2, 3, 4, 5, 6)
print(get_sum(results))
print(get_average(results))

