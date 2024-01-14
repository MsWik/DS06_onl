# # 3
# # Напишите функцию multiplication_matrix, которая принимает размер матрицы (N)
# # и возвращает массив описывающий таблицу умножения N на N.

def multiplication_matrix(n):
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

if __name__ == "__main__":
    print(multiplication_matrix(3))