import numpy as np
deka_x,deka_y = map(float,input("Введите координаты Деки в декартовых координатах через пробел: ").split())
deka_dekart = np.array([deka_x, deka_y])

ρ,ϕ = map(float,input("Введите координаты Поли в полярных координатах ρ, ϕ (в градусах) через пробел: ").split())
poly_polar = np.array([ρ, ϕ])


phi = np.radians(poly_polar[1])
poly_dekart= np.array([poly_polar[0] * np.cos(phi), poly_polar[0] * np.sin(phi)])


distance = np.sqrt((deka_dekart[0]-poly_dekart[0])**2+(deka_dekart[1]-poly_dekart[1])**2)

print("Кратчайшее расстояние между Декой и Полей:", distance)