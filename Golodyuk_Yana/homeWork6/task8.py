# Задача 8

# Разработайте декоратор same_type, который производит проверку переменного
# количества позиционных параметров. В случае получения не одинаковых типов
# выводит сообщение "Обнаружены различные типы данных" и прерывает выполнение функции.


def same_type(f):
    def decorated(*args, **kwargs):
        # проверить тип
        if len({type(x) for x in args}) == 1:
            return f(*args, **kwargs)
        else:
            # print('Обнаружены различные типы данных')
            raise AttributeError("Обнаружены различные типы данных")

    return decorated


@same_type
def a_plus_b(*args):
    return f"{sum(args)}"


if __name__ == "__main__":
    print(a_plus_b(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1.0))