from math import sin, cos
deka = [int(i) for i in input().split()]
poly =  [int(i) for i in input().split()]
x_poly = poly[0] * cos(poly[1])
y_poly = poly[0] * sin(poly[1])
ans = (abs((deka[0] + x_poly))**2 + abs((deka[1] + y_poly))**2)**(1/2)
print(ans)