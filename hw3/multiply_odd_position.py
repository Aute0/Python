## Задача №1: Задайте список из нескольких чисел. Напишите программу, которая найдёт
#  сумму элементов списка, стоящих на нечётной позиции.
#  Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
print('Находим сумму элементов из вашего списка, стоящих на нечетных позициях')
my_list = [randint(-10, 10) for i in range(20)]
print("Ваш список чисел " , my_list)

odd_sum=[]

for i in range(0,len(my_list),2):
    odd_sum = sum(my_list)
print('Список чисел, стоящих на нечетных позициях', my_list[1::2])
print('Сумма нечетных элементов вашего списка', odd_sum)
