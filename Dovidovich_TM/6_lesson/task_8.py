def same_types(f):
    def decorated(*args):
        types = set(type(arg) for arg in args)
        if len(types) != 1:
            print("Обнаружены различные типы данных")
            return
        return f(*args)
    return decorated


@same_types
def function(a, b):
    print(a+b)


def task_8():
    function(3, 5)


if __name__ == '__main__':
    task_8()
