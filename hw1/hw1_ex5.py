## Задача №5: Напишите программу, которая принимает на вход координаты двух точек и находит
#  расстояние между ними в 2D пространстве.

print('Введите координаты точки А: ')
x_a = int(input(' x_a =  '))
y_a = int(input(' y_a =  '))

print('Введите координаты точки B: ')
x_b = int(input(' x_b =  '))
y_b = int(input(' y_b =  '))

coords_between_dots = ((x_b - x_a)**2 + (y_b - y_a)**2)**(1 / 2)
print('Расстояние между точками А и В: ')
print(round(coords_between_dots,3))