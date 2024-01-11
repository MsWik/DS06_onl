def solve():
    s = input()
    n = s[0]
    sum = 0
    for i in s:
        if n == i:
            n = i
            sum += 1
        else:
            print(n,sum)
            n = i
            sum = 1
    print(n,sum)

if __name__ == '__main__':
    solve()