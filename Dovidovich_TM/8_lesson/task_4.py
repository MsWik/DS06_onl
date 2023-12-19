import numpy as np

#np.array([np.roll(np.array([0,1,0,1,0,1,0,1]), i) for i in range(np.array([0,1,0,1,0,1,0,1]).shape[0])])
def stairs(array: np.ndarray) -> np.ndarray:
    return np.array([np.roll(array, i) for i in range(array.shape[0])])


def main():
    print(stairs(np.arange(5)))


if __name__ == '__main__':
    main()
