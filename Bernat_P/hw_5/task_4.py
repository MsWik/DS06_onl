print(500)
n = 500
a = 1
b = 1000
step = 2
for i in range(10):
    s = input()
    if s == 'b':
        a = b
        b = round(2 * b-abs((b-a)/2) )
        print(b)
    elif s == 'm':
        b = round(b-abs((b-a)/2))
        print(b)
    elif s == 'ok':
        break

    