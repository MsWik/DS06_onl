class Rectangle:

    def __init__(self,pos_1,pos_2) -> None:
        self.pos_1 = pos_1
        self.pos_2 = pos_2

    def perimeter(self):
        return round(2*(abs(self.pos_1[0] - self.pos_2[0]) + abs(self.pos_1[1] - self.pos_2[1])),2)
    

    def area(self):
        return round((abs(self.pos_1[0] - self.pos_2[0]) * abs(self.pos_1[1] - self.pos_2[1])),2)


    def get_pos(self):
        return self.pos_1[0],self.pos_2[1]
    

    def get_size(self):
        return round(abs(self.pos_1[0] - self.pos_2[0]),2), round(abs(self.pos_1[1] - self.pos_2[1]),2)


    def move(self,dx,dy):
        pass




if __name__ == '__main__':

    rect = Rectangle((3.2, -4.3), (7.52, 3.14))
    print(rect.get_pos(), rect.get_size())
    rect.move(1.32, -5)
    print(rect.get_pos(), rect.get_size())