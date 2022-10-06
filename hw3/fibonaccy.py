## Задача №5: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Ищем по формуле Бине: Формула Бине — это формула, которая может использоваться для вычисления
# n-го члена последовательности Фибоначчи, а это именно то, что мы хотим сделать;
# эта формула названа в честь открывшего её французского математика Жака Филиппа Мари Бине.

import decimal
n = int(input('Введите число n: '))


def fib_nums(n):
    list_fnums = []
    a, b = 1, 1
    for i in range(n-1):
        list_fnums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n+1):
        list_fnums.insert(0, a)
        a, b = b, a - b
    return list_fnums


list_fnums = fib_nums(n)
print(fib_nums(n))
print(list_fnums.index(0))

# Вычисление n-ого числа по формуле Бине:

### for i in range(1, n):
    # Формула Бине
   #  F = int((((1+5**0.5)/2) ** i - ((1-5**0.5)/2) ** i) / 5**0.5)
   #  print(F)