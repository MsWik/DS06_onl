import numpy as np

#Normalize a 5x5 random matrix (★☆☆)
matrix = np.random.rand(5, 5)
print(matrix)
min_val = np.min(matrix)
max_val = np.max(matrix)
normalized_matrix = (matrix - min_val) / (max_val - min_val)
print(normalized_matrix)