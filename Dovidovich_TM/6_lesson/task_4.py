def task_4():
    string = 'ббб аа ббааа'.lower()
    print(sorted(string.split(), key=lambda x: len(x)))
    print(sorted(string.split(), key=lambda x: x))


if __name__ == '__main__':
    task_4()
