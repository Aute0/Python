## Задача №5: Даны два файла, в каждом из которых находится запись многочлена. 
#  Задача - сформировать файл, содержащий сумму многочленов.

import re
from random import randint
import itertools
#------------------------------------------------------------------------
print('Программа выведет результат суммы двух полиномов из файлов')
power = int(input('Введите степень полинома №1: '))
list_coeff = [randint(-5, 10) for n in range(1, power+1)
              ]  # задаем список коеффициентов
print("Список ваших коеффициентов: ")
print(list_coeff)

def create_polinome(power, list_coeff):  # создаем полином
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

with open('poli1.txt', 'w') as data:
    data.write(polynom1)
#------------------------------------------------------------------------
# Второй многочлен для задачи:

power2 = int(input('Введите степень полинома №2: '))
list_coeff2 = [randint(-5, 20) for n in range(1, power2+1)]  # задаем список коеффициентов
print("Список ваших коеффициентов: ")
print(list_coeff2)
polynom2 = create_polinome(power2, list_coeff2)
print(polynom2)

with open('poli2.txt', 'w') as data:
    data.write(polynom2)
#------------------------------------------------------------------------
file1 = 'poli1.txt'
file2 = 'poli2.txt'
file_sum = 'poli_summ.txt'
#------------------------------------------------------------------------
# Забираем данные обратно из файла
def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol
#------------------------------------------------------------------------
# Получение коеффициентов и степеней
def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
#   убрали все символы
    for i in pol:
        if i[0] == 'x':
            i.insert(0, 1)
        if i[-1] == 'x':
            i.append(1)
        if len(i) == 1:
            i.append(0)
#   получили коеффициенты и степени
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol
#------------------------------------------------------------------------
# Получение степеней и коеффициентов суммы полиномов
def fold_pols(pol1, pol2):
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key=lambda r: r[1], reverse=True)
    return res
#------------------------------------------------------------------------
# Итоговый многочлен
def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)]
               for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0':
            del (x[0])
        if x[-1] == '0':
            del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^':
            del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1':
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))
#------------------------------------------------------------------------
def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)
#------------------------------------------------------------------------
pol1 = read_pol(file1)
pol2 = read_pol(file2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
write_to_file(file_sum, pol_sum)
print("Многочлен №1: ")
print(pol1)
print("Многочлен №2: ")
print(pol2)
print("Результат суммы двух полиномов: ")
print(pol_sum)
