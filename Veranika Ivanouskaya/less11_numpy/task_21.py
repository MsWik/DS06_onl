import numpy as np

#Create a checkerboard 8x8 matrix using the tile function (★☆☆)
base = np.array([[0, 1], [1, 0]])
print(base)
checkerboard = np.tile(base, (4, 4))
print(checkerboard)