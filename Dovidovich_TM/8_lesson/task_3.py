import numpy as np


def multiplication_matrix(a: int) -> np.ndarray:
    return np.array([[i*j for i in range(1, a+1)] for j in range(1, a+1)])


def main():
    print(multiplication_matrix(5))


if __name__ == '__main__':
    main()
