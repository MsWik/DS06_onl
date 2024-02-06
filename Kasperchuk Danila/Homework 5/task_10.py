def main():
    n = int(input())
    square = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            value = min(i, j, n - i - 1, n - j - 1) + 1
            square[i][j] = value

    for row in square:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    main()