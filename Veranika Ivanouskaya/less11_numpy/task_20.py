import numpy as np

#Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
index_to_find = 100
shape = (6, 7, 8)
print(shape)
index_xyz = np.unravel_index(index_to_find, shape)
print(index_xyz)