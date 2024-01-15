# # 1
# # Класс Rectangle


class Rectangle:
    def __init__(self, point_1, point_2):
        point_1, point_2 = sorted([point_1, point_2], key=lambda x: x[0])
        self.point_1 = point_1
        self.point_2 = point_2

        dx = self.get_dx()
        dy = self.get_dy()

        if not self.point_1[1] > self.point_2[1]:
            self.point_1 = (self.point_1[0], self.point_1[1] + dy)
            self.point_2 = (self.point_2[0], self.point_2[1] - dy)

    def get_dx(self):
        return abs(round(self.point_1[0], 2) - round(self.point_2[0], 2))

    def get_dy(self):
        return abs(round(self.point_1[1], 2) - round(self.point_2[1], 2))

    def get_pos(self):
        if self.point_1[1] > self.point_2[1]:
            return self.point_1
        return self.point_1[0], self.point_2[1] + self.get_dy()

    def get_size(self):
        return (self.get_dx(), self.get_dy())

    def move(self, dx, dy):
        self.point_1 = (round(self.point_1[0] + dx, 2), round(self.point_1[1] + dy, 2))
        self.point_2 = (round(self.point_2[0] + dx, 2), round(self.point_2[1] + dy, 2))

    def resize(self, width, height):
        self.point_2[0] = self.point_1[0] + width
        self.point_2[1] = self.point_1[1] - height

    def perimetr(self):
        dx = self.get_dx()
        dy = self.get_dy()
        return 2 * (dx + dy)

    def area(self):
        dx = self.get_dx
        dy = self.get_dy
        return dx * dy


if __name__ == "__main__":
    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    print(round(rect.perimetr(), 2))
    print(rect.get_pos(), rect.get_size())
    rect.move(1.32, -5)
    print(rect.get_pos(), rect.get_size())

# # Вывод

# # (3.2, 3.14) (4.32, 7.44)
# # (4.52, -1.86) (4.32, 7.44)