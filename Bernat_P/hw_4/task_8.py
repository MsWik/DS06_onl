def solve():    
    a = int(input())
    b = int(input())
    s = []
    for i in range(a,b+1):
        s.append(a*a)
        a += 1
    print(s)


if __name__ == '__main__':
    solve()