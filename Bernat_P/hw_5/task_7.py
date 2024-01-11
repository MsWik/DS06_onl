def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
ans = []
n = int(input())
for number in range(1,n):
    if is_prime(number):
        ans.append(number)
print(ans,len(ans))