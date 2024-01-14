# Задача 9

# Напишите генератор cycle, который принимает список и работает аналогично итератору itertools.cycle.

def cycle(l):
    while True:
        for elm in l:
            yield elm

if __name__ == "__main__":
    print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))