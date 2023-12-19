def main():
    number = input()
    target = number[0]
    counter = 0
    for digit in number:
        if target == digit:
            counter +=1
        else:
            print(target, counter)
            target = digit
            counter = 1
    print(target, counter)    


if __name__ == "__main__":
    main()
