import numpy as np

#Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★)
array1 = np.random.rand(5, 5, 3)
array2 = np.random.rand(5, 5)
result = array1 * array2[:, :, np.newaxis]
print(result)
