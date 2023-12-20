def main():
    number_a = int(input())
    number_b = int(input())
    answer = list()
    print([number**2 for number in range(number_a,number_b+1)])


if __name__ == "__main__":
    main()
