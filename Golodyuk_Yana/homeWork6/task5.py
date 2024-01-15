# Задача 5

# Напишите lambda выражение для фильтрации чисел с чётной суммой цифр.

def filtered_numbers(List):
    print(*filter(lambda x: sum(map(int, list(str(x)))) % 2 == 0, List))

if __name__ == "__main__":
    numbers = [1, 5, 11, 35, 67]
    filtered_numbers(numbers)