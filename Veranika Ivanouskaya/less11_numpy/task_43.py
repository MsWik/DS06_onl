import numpy as np

#Make an array immutable (read-only) (★★☆)
array = np.array([1, 2, 3])
array.flags.writeable = False
try:
    array[0] = 5
except ValueError as e:
    print(e)