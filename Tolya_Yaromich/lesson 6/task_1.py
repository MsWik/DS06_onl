""""Напишите функцию make_matrix, которая создаёт, заполняет и возвращает матрицу заданного размера.
Параметры функции:
size — кортеж (ширина, высота) или одно число (для создания квадратной матрицы); 
value — значение элементов списка (по-умолчанию 0)."""

def make_matrix(size, value=0):
    if isinstance(size, int):
        matrix = [[value] * size for _ in range(size)]
    elif len(size) == 2 and all(isinstance(i, int) for i in size):
       
        matrix = [[value] * size[0] for _ in range(size[1])]
    else:
        raise ValueError("Некорректные параметры size. Допустимые форматы: int или (int, int).")
    return matrix
matrix1 = make_matrix(3) 
print(matrix1)

matrix2 = make_matrix((2, 4), value=1)  
print(matrix2)
