# # 2
# # Формат ввода В первой строке записаны координаты Деки: два рациональных числа —
# # Во второй строке записаны координаты Поли: два рациональных числа —
# # Формат вывода Одно число — расстояние между Декой и Полей.

import numpy as np

def distance():

    x, y = map(float, input().split())
    r, phi = map(float, input().split())

    x_2 = r * np.cos(phi)
    y_2 = r * np.sin(phi)

    print(((x - x_2) ** 2 + (y - y_2) ** 2) ** 0.5)

if __name__ == "__main__":
    distance()