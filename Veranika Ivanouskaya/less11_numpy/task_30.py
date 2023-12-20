import numpy as np

#How to find common values between two arrays? (★☆☆)
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([3, 4, 5, 6, 7])
common_values = np.intersect1d(array1, array2)

print(common_values)