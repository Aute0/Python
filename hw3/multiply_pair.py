## Задача №2: Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#  Пример:  - [2, 3, 4, 5, 6] = > [12, 15, 16]
#              - [2, 3, 5, 6] = > [12, 15]

print('Ищем произведение пар чисел в списке')

from random import randint 
import math

my_list = [randint(-10, 10) for i in range(4)]
print("Ваш список чисел ", my_list)

mult_pair = []
for i in range(math.ceil(len(my_list)/2)):
    mult_pair = my_list[i]*my_list[-i-1]
    print(mult_pair)
