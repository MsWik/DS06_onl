def task_5():
    numbers = [123, 234, 9242, 14345]
    sum_even = list(filter(lambda x: sum(
        map(int, list(str(x)))) % 2 == 1, numbers))
    print(sum_even)


if __name__ == '__main__':
    task_5()
