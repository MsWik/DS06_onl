# Шахматный «обед»
#
# Напишите функцию can_eat, которая принимает положение коня и другой фигуры в виде кортежей из двух координат,
# а возвращает булево значение: True если конь съедает фигуру и False иначе.
# Ввод
# result = can_eat((2, 1), (4, 2))
# Вывод
# result = True

def can_eat(hrs, fig: tuple) -> bool:
    hrs_x, hrs_y = hrs
    fig_x, fig_y = fig
    dx = abs(hrs_x - fig_x)
    dy = abs(hrs_y - fig_y)
    return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

# Пример использования
result = can_eat((2, 1), (4, 2))
print(result)