# 14. Подсчитать сумму цифр в вещественном числе.

from random import uniform

n = round(uniform(1, 100), 3)

def sum_digit(n):
    return sum(map(int, list(str(n).replace('.', ''))))

print(n)
print(sum_digit(n))

# Предыдущее решение
##  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#   Пример: - 6782 -> 23
#           - 0,56 -> 11

#   UserNumber = float(input('Введите число:  '))
#   def sumNums(UserNumber):
#       sum = 0
#       for i in str(UserNumber):
#           if i != ".":
#               sum += int(i)
#       return sum

#   print(f"Сумма цифр = {sumNums(UserNumber)}")
