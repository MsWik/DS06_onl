def main():
    s_splitted = list(input())
    result = sum([int(i) for i in s_splitted])

    return result

if __name__ == '__main__':
    print(main())