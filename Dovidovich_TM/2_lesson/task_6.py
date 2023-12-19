def task_6():
    number_red, number_green, number_blue = map(int, input().split())
    print(number_red+number_blue+1) if number_green>0 else print('infinity')


if __name__ == '__main__':
    task_6()
