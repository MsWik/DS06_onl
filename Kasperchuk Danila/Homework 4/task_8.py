def main():
    n = int(input())
    m = int(input())
    list_values = range(n, m+1)
    total = [i**2 for i in list_values]
    return total

if __name__ == '__main__':
    print(main())