def main(amount):
    count = 0
    for i in range(amount):
        str = input().split(" ")
        for j in str:
            if j == "зайка":
                count += 1

    return count


if __name__ == '__main__':
    amount = int(input())
    print(main(amount))