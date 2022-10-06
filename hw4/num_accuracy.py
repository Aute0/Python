## Задача №1: Вычислить число c заданной точностью d
# Пример: - при d = 0.001, π = 3.141
#           10 ^ {-1} ≤ d ≤10 ^ {-10}

from decimal import *
from math import factorial

print("Программа выведет значения числа Пи с заданной вами точностью")

# Число пи считаем по формуле Чудновского

def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k) * (Decimal(factorial(6 * k)) / ((factorial(k)**3)
                                                               * (factorial(3*k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
        k += 1
        print("Шаг: {} из {}".format(k, n))
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return pi


# Требуемая точность (число знаков)
N = int(input('Введите число знаков после запятой:  '))
getcontext().prec = N+1
val = chudnovsky(N / 14)
print(val)

