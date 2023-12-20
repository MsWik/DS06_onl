import numpy as np
#------29
arr = np.array([-3.14, -2.5, -1.7, 0, 1.2, 3.8])
rounded_up = np.ceil(np.abs(arr)) * np.sign(arr)

print(rounded_up)


#------30
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([3, 4, 5, 6, 7])

common_values = np.intersect1d(arr1, arr2)

print(common_values)
#------31
#----np.seterr(all='ignore')

# Вернуть обратно настройки по умолчанию (необязательно)
#----np.seterr(all='warn')

#------35
import numpy as np

A = np.array([1, 2, 3], dtype='float64')
B = np.array([4, 5, 6], dtype='float64')
A += B
A *= -A / 2
print(A)
#------36

random_array = np.random.rand(5) * 10  
# Метод 1: Использование функции astype
method_1 = random_array.astype(int)

# Метод 2: Использование numpy.floor
method_2 = np.floor(random_array).astype(int)

# Метод 3: Использование numpy.ceil
method_3 = np.ceil(random_array - 0.5).astype(int)

# Метод 4: Использование numpy.trunc
method_4 = np.trunc(random_array).astype(int)

print("Исходный массив:", random_array)
print("Метод 1 (astype):", method_1)
print("Метод 2 (floor):", method_2)
print("Метод 3 (ceil):", method_3)
print("Метод 4 (trunc):", method_4)

#------37
he = np.tile(np.arange(0, 5), (5, 1))
print(he)

#------38
import numpy as np

def generate_random_integers():
    return np.random.randint(0, 100, 10)
generated_array = generate_random_integers()
print(generated_array)
#------39
vek=np.linspace(0, 1, 12)[1:-1]
print(vek)
#------40
print(np.sort(generated_array))
#------41
print(np.add.reduce(generated_array))
#------42
Xa=np.random.randint(0, 100, np.random.randint(3,13))
Xb=np.random.randint(0, 100, np.random.randint(3,13))
print(np.array_equal(Xa, Xb))
#------43
generated_array.flags.writeable = False
generated_array.flags.writeable = True
#------44
cartesian_coordinates = np.random.rand(10, 2)
x, y = cartesian_coordinates[:, 0], cartesian_coordinates[:, 1]
r = np.sqrt(x**2 + y**2)
fi = np.arctan2(y, x)
polar_coordinates = np.column_stack((r, fi))
print("Декартовы координаты:")
print(cartesian_coordinates)
print("\nПолярные координаты:")
print(polar_coordinates)
#------45
random_array = np.random.uniform(1, 30, size=(10,))
print(random_array)
random_array[random_array.argmax()]=0
print(random_array)
