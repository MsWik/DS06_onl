import numpy as np 


def geometric_mean(x):
    product = np.prod(x)
    geometric_mean = product ** (1/len(x))
    return geometric_mean


x = np.array([2, 3, 4, 5])


