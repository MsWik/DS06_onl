def main():
    number_a = int(input())
    number_b = int(input())
    dictionary = dict()

    for _ in range(number_a):
        second_name = input()
        dictionary[second_name] = []
        dictionary[second_name].append("манная")

    for _ in range(number_b):
        second_name = input()
        if second_name not in dictionary:
            dictionary[second_name] = []
        dictionary[second_name].append("овсянка")

    counter = 0
    for _, elements in dictionary.items():
        if len(elements) == 1:
            counter += 1

    print(counter) if counter else print("Таких нет")


if __name__ == "__main__":
    main()
