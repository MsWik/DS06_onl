def main():
    list_nums = list(input())
    prepared_list = [int(i) for i in list_nums]
    result = []

    for num in prepared_list:
        if num % 2 != 0:
            result.append(num)
        else:
            continue

    result = [str(j) for j in result]
    return "".join(result)

if __name__ == '__main__':
    print(main())