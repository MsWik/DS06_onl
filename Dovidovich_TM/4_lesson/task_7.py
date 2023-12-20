def main():
    dictionary = dict()
    while True:
        pair = input().split()
        if pair:
            if pair[0] not in dictionary:
                dictionary[pair[0]] = set()
            if pair[1] not in dictionary:
                dictionary[pair[1]] = set()
            dictionary[pair[0]].add(pair[1])
            dictionary[pair[1]].add(pair[0])
        else:
            break

    for key, elements in dictionary.items():
        relations = dict()
        relations[key] = set()
        for element in elements:
            for person in dictionary[element]:
                if person not in dictionary[key] and person != key:
                    relations[key].add(person)
        print(key, ": ", end="")
        print(*relations[key], sep=", ")


if __name__ == "__main__":
    main()
