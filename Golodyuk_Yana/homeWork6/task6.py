# Задача 6

# Напишите рекурсивную функцию для вычисления n-го числа последовательности Фибоначчи.

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print(fibonacci(15))