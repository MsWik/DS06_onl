def solve():
    x = int(input())
    y = int(input())
    s1 = []
    s2 = []
    value = 0
    ans = ''
    for i in range(x):
        s1.append(input())
    for i in range(y):
        s2.append(input())
    for name in s1:
        if name in s2:
            value -= 2
            if value == -(x+y):
                print('Таких нет')
                break
    print(x + y + value)


if __name__ == '__main__':
    solve()
