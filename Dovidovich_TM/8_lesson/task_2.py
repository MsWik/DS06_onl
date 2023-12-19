import numpy as np
from typing import Tuple


def get_decart_coordinates(p: np.float64, f: np.float64) -> Tuple[np.float64, np.float64]:
    return p*np.cos(f), p*np.sin(f)


def get_length(x_1: np.float64, y_1: np.float64, p: np.float64, f: np.float64) -> np.float64:
    x_2, y_2 = get_decart_coordinates(p, f)
    return np.sqrt((x_1-x_2)**2+(y_1-y_2)**2)


def main():
    x, y = tuple(map(np.float64, input().split()))
    p, f = tuple(map(np.float64, input().split()))
    length = get_length(x, y, p, f)
    print(length)


if __name__ == '__main__':
    main()
