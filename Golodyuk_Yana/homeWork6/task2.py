# Задача 2

# Напишите функцию make_matrix, которая создаёт, заполняет и
# возвращает матрицу заданного размера.
# Параметры функции:
# size — кортеж (ширина, высота) или одно число (для создания квадратной матрицы);
# value — значение элементов списка (по-умолчанию 0).

def make_matrix(size, value=0):
  if isinstance(size, tuple):
    return [[value for _ in range(size[0])] for _ in range(size[1])]
  return [[value for _ in range(size)] for _ in range(size)]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    matrix = make_matrix(5, -15)
    print_matrix(matrix)