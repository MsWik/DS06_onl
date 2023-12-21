import numpy as np

'''a = np.array([1, 2, 3, 4])
b = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(f"a[0] = {a[0]}")
print(f"b[0] = {b[0]}")


a = np.array([1, 2, 3], dtype="uint8")
a[0] = 260
print(a)

a = np.array([1, 2.5, 3])
print(a)
print(a.dtype)
b = np.array(['text', 1, 2.5])
print(b)
print(b.dtype)

a = np.zeros((4, 3))
print(a)
print(a.dtype)
print()
a = np.zeros((4, 3), dtype="int32")
print(a)

a = np.ones((4, 3))
print(a)

a = np.eye(5, 3, dtype="int8")
print(a)

a = np.arange(1, 10)
print(a)
print()
a = np.arange(1, 5, 0.4)
print(a)

a = np.linspace(1, 5, 40)  # задаётся начало, конец диапазона и количество значений
print(a)

a = np.array([[1,2,3],[4,5,6]])

print(a)
print()

a = a.reshape((6, 1))
print(a)

a = np.zeros((4, 3), dtype="uint8")
print(a)
print()
a = a.reshape((2, 6))
print(a)


a = np.zeros((4, 3), dtype="uint8")
print(a)
print()
a.resize((2, 2, 3))
print(a)'''

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0]])
print(a @ b)