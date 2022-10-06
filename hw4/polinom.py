## Задача №4: Задана натуральная степень power. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени power. 
#  Пример: - power = 2 = > 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import itertools

print('Программа выведет полином с коеффициентами, сформированными случайным образом. Степень полинома Вы задаете сами')
power = int(input('Введите степень полинома: '))
list_coeff = [randint(-5, 10) for n in range(1, power+1)] #задаем список коеффициентов
print("Список ваших коеффициентов: ")
print(list_coeff)

def create_polinome(power, list_coeff): # создаем полином 
    var = ['*x^']*(power-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(
        list_coeff, var, range(power, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')
# itertools.zip_longest сливает коеффициенты, х, и все что нужно, при этом заполняет пустые места пробелом (в данном случае)
polynom1 = create_polinome(power, list_coeff)
print(polynom1)