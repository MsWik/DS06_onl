#Напишите функцию is_prime, которая принимает натуральное число, а возвращает булево значение:
# True — если переданное число простое, а иначе — False.

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

result = is_prime(int(input()))
print(result)