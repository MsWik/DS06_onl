def main():
    list_places = []
    for i in range(3):
        list_places.append(input())

    for string in list_places:
        if "зайка" in string:
            return f"{string} {len(string)}"
        else:
            continue

if __name__ == '__main__':
    print(main())