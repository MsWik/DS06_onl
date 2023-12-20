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

if __name__ == '__main__':
    task_5()