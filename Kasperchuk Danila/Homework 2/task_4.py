def main():
    list_of_letters = list(input())
    list_of_letters[0], list_of_letters[1] = list_of_letters[1], list_of_letters[0]
    list_of_letters[2], list_of_letters[3] = list_of_letters[3], list_of_letters[2]
    return "".join(list_of_letters)

if __name__ == '__main__':
    print(main())