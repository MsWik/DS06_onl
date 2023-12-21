import numpy as np

#Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
array = np.zeros((8, 8), dtype=int)
array[::2, 1::2] = 1
array[1::2, ::2] = 1
print(array)
