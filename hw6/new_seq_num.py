from msilib import sequence

n = int(input('Введите число: '))

def get_sequence(n):
    return [round((1 + 1 / x)**x, 5) for x in range(1, n + 1)]

nums = get_sequence(n)
print(nums)
print(round(sum(nums), 5))

# Предыдущее решение

###  Задайте список из n чисел последовательности $(1 +\frac 1 n) ^ n$ и выведите на экран их сумму.
#   Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

#   print('Программа выводит последовательность чисел типа (1+1/n)^n и сумму всех чисел до указанного n')
#   UserNumber = int(input('Введите n:  '))
#   UserList = [round(((1+1/n)**n), 3) for n in range(1, UserNumber+1)]
#   print(F'Ваша числовая последовательность: {UserList}')
#   sum = 0
#   for i in range(0, len(UserList)):
#       sum += UserList[i]
#   print(F"Сумма чисел в последовательности = {round(sum,3)}")