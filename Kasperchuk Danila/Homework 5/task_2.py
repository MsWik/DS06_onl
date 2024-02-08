def main():
    # можно использовать max но я хочу написать свой алгоритм
    n = list(input())
    prepared_list = [int(i) for i in n]
    max_num = 0
    for j in prepared_list:
        if j > max_num:
            max_num = j
        else:
            continue
    return max_num

if __name__ == '__main__':
    print(main())