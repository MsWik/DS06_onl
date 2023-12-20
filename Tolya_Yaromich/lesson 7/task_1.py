class Rectangle:
    def __init__(self, point1, point2):
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2

    def perimeter(self):
        length = abs(self.x2 - self.x1)
        width = abs(self.y2 - self.y1)
        return round(2 * (length + width), 2)

    def area(self):
        length = abs(self.x2 - self.x1)
        width = abs(self.y2 - self.y1)
        return round(length * width, 2)


point1 = (1, 2)
point2 = (4, 6)
rect = Rectangle(point1, point2)

print("Периметр прямоугольника:", rect.perimeter())
print("Площадь прямоугольника:", rect.area())
