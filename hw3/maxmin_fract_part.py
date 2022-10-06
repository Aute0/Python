## Задача №4: Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] = > 0.19


from random import uniform
import math

user_list = [round(uniform(-5, 5), 2) for i in range(6)]
print("Ваш список чисел ", user_list)

list_fract = [round(x-math.trunc(x),2) for x in (user_list)]
print('Максимальная дробная часть: ')
print(max(list_fract))

print('Минимальная дробная часть: ')
print(min(list_fract))

diff = round((max(list_fract)-min(list_fract)),2)

print('Разность между максимальной и минимальной: ')
print(diff)

