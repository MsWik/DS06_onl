# Шахматный «обед»
# Напишите функцию can_eat, которая принимает
# положение коня и другой фигуры в виде кортежей
# из двух координат, а возвращает булево 
# значение: True если конь съедает фигуру и False иначе.
# Ввод
# result = can_eat((2, 1), (4, 2))
# Вывод
# result = True

def cat_eat(h_pos,other_pos):
    x,y = h_pos
    x1,y1 = other_pos
    if abs(x-x1) + abs(y-y1) == 3:
        return True
    return False




if __name__ == '__main__':
   print(cat_eat((0,1),(-2,-1)))

