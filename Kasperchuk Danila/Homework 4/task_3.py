def main():
    n = input()
    n = n.split()
    new_n = [int(i) for i in n]
    return sum(new_n)

if __name__ == '__main__':
    print(main())