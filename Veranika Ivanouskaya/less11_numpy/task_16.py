import numpy as np

#How to add a border (filled with 0's) around an existing array? (★☆☆)
array = np.ones((5, 5), dtype=int)
print(array)
new_array = np.zeros((7, 7), dtype=int)
print(new_array)
new_array[1:-1, 1:-1] = array
print(new_array)