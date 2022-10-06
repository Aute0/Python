## Задача №3: Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
print('Программа выведет список неповторяющихся эл-ов в последовательности')
size = int(input('Введите размер последовательности n: '))
rand_list = [randint(-5,10) for n in range(1, size+1)]

print('Ваша последовательность чисел: ')
print(rand_list)

def get_unic_value(rand_list):
    return [i for i in set(rand_list)]

origin = get_unic_value(rand_list)
print('Уникальные числа вашей последовательности: ')
print(origin)
