def task_1():
    input_value = list(input())
    print("".join(input_value[::-1]))


def task_2():
    input_numbers = input().split()
    print(" ".join(input_numbers[::-1]))


def task_3():
    N = int(input())
    for i in range(N):
        print('*'*N)


def task_4():
    digits_list = list(input())
    digits_list.reverse()
    digits_list = digits_list[2:4]+digits_list[0:2]
    print("".join(digits_list))


def task_5():
    number_1 = list(input())
    number_2 = list(input())
    sum_result = []
    min_length = min(len(number_1), len(number_2))
    for i in range(-min_length, 0, 1):
        digit_sum = (int(number_1[i])+int(number_2[i])) % 10
        sum_result.append(str(digit_sum))
    longest_list = max(number_1, number_2)
    print("".join(longest_list[:-min_length])+"".join(sum_result))


def task_6():
    number_red, number_green, number_blue = map(int, input().split())
    print(number_red+number_blue+1)


def task_7():
    number_A = 10
    number_B = 32
    number_C = 5
    result = abs(number_A-number_B)/number_C
    print("{0:.2f}".format(result))


def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()


if __name__ == '__main__':
    main()
