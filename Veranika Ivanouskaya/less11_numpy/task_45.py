import numpy as np

#Create random vector of size 10 and replace the maximum value by 0 (★★☆)
vector = np.random.random(10)
print(vector)
max_index = np.argmax(vector)
vector[max_index] = 0
print(vector)