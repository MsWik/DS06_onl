def task_4():
    digits_list = list(input())
    digits_list.reverse()
    digits_list = digits_list[2:4]+digits_list[0:2]
    print("".join(digits_list))

    
if __name__ == '__main__':
    task_4()