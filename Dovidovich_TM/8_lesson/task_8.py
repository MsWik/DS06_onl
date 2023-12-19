import numpy as np
import pandas as pd
from decimal import Decimal


def values(function, start: float, end: float, step: float) -> pd.Series:
    results = []
    x_args = []
    x = start
    digits = Decimal(str(step)).as_tuple().exponent*(-1)
    # без round работать не будет. проклятая мантисса :C 1.7000000000000008 > 1.7
    while round(x, digits) <= end:
        x_args.append(x)
        results.append(function(x))
        x += step
    df = pd.Series(results, index=x_args)
    return df


def min_extremum(df: pd.Series) -> np.float64:
    return df[(df[:] == df.min())].index[0]


def max_extremum(df: pd.Series) -> np.float64:
    return df[(df[:] == df.max())].index[0]


def main():
    data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.01)
    print(data)
    print(min_extremum(data))
    print(max_extremum(data))


if __name__ == '__main__':
    main()
