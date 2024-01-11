def solve():
    n = [int(i) for i in input().split() ]
    # print(sum(n))
    sum = 0
    for i in n:
        sum += i
    print(sum)


if __name__ == '__main__':
    solve()

