def main():
    number = int(input())
    dictionary = dict()
    for _ in range(number):
        string = input().lower()
        for element in string.split():
            if element in dictionary:
                dictionary[element] += 1
            else:
                dictionary[element] = 1
    print(dictionary['зайка'])

if __name__ == "__main__":
    main()
