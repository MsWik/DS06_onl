def main():
    num_1 = list(input())
    num_2 = list(input())
    summ_first = (int(num_1[2]) + int(num_2[2])) % 10 if int(num_1[2]) + int(num_2[2]) > 10 else int(num_1[2]) + int(num_2[2])
    summ_second = (int(num_1[1]) + int(num_2[1])) % 10 if int(num_1[1]) + int(num_2[1]) > 10 else int(num_1[1]) + int(num_2[1])
    summ_third = (int(num_1[0]) + int(num_2[0])) % 10 if int(num_1[0]) + int(num_2[0]) > 10 else int(num_1[0]) + int(num_2[0])
    total = str(summ_third) + str(summ_second) + str(summ_first)
    return total

    # Думаю код не очень хороший, получился слишком ьбольшим
if __name__ == '__main__':
    print(main())