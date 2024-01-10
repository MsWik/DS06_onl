def solve():
    n = int(input())
    zaika = 0
    for _ in range(n):
        s = input().split()
        for word in s:
            if word == 'зайка':
                zaika += 1
    print(zaika)

if __name__ == '__main__':
    solve()

