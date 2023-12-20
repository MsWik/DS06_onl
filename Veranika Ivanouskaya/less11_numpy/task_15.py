import numpy as np

#Create a 2d array with 1 on the border and 0 inside (★☆☆)
array = np.ones((10, 10), dtype=int)
print(array)
array[1:-1, 1:-1] = 0
print(array)
