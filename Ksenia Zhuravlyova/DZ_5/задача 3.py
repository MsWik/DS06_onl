#Напишите функцию make_matrix, которая создаёт, заполняет и возвращает матрицу заданного размера.
#Параметры функции:
#size — кортеж (ширина, высота) или одно число (для создания квадратной матрицы);
# value — значение элементов списка (по-умолчанию 0).
def make_matrix(size, value=0):
    if isinstance(size, int):
        width = height = size
    else:
        width, height = size

    matrix = [[value] * width for _ in range(height)]
    return matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()
matrix_size = (4, 6)
matrix = make_matrix(matrix_size, 0)
print_matrix(matrix)