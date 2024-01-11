def same_type (f):
    def decoreted (*args, **kwargs):
        if type(args[0]) == type(args[1]):
            return f(*args, **kwargs)
        else:
            return 'Обнаружены различные типы данных'
    return decoreted
@same_type
def a_plus_b (a,b):
    return a+b

if __name__ == '__main__':
    print(a_plus_b(1,[12]))

