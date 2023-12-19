import numpy as np


def main():
    values = list(map(int, input().split()))
    print("{:.15f}".format(np.exp(np.mean(np.log(values)))))


if __name__ == '__main__':
    main()
