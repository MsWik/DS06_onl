num = [int(i) for i in input().split()]
print(num)
ans = 1
for i in num:
    ans *= i

print('{:.5f}'.format(ans ** (1/len(num))))
