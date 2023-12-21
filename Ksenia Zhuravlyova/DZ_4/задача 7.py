
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


N = int(input())

prime_count = 0

for _ in range(N):
    num = int(input())
    if is_prime(num):
        prime_count += 1

print(prime_count-1)