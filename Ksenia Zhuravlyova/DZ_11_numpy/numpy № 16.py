# Как добавить границу (заполненную нулями) вокруг существующего массива (например:
# массив 5 на 5 из единиц окружить нулями,чтобы он превратился в массив 7 на 7?


import numpy as np
а = np.ones((5,5), dtype=int)
print(а)
print()
а = np.pad(а, pad_width=1, mode='constant', constant_values=0)
print(а)