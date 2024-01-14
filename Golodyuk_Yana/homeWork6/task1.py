# Задача пример
# Напишем функцию, которая проверяет,
# что список целых чисел, передаваемый ей как аргумент,
# содержит только чётные числа

# from typing import List, Union, Tuple

# def are_all_even_numbers(numbers: List[int]) -> Union[bool, Tuple[bool, int]]:
#     for i, num in enumerate(numbers):
#         if num % 2 != 0:
#             return False, i
#     return True

# if __name__ == "__main__":
#     print(are_all_even_numbers([10, 3, 2, 4]))


# Задача 1

# Шахматный «обед»
# Напишите функцию can_eat, которая принимает положение коня и другой фигуры
# в виде кортежей из двух координат, а возвращает булево значение:
# True если конь съедает фигуру и False иначе.
# Ввод
# result = can_eat((2, 1), (4, 2))
# Вывод
# result = True

def can_eat(a, b):
  l = [abs(a[0] - b[0]), abs(a[1] - b[1])]
  return sorted(l) == [1, 2]

if __name__ == "__main__":
    print(can_eat((2,2), (4,2)))