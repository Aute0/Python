##  Задайте список из n чисел последовательности $(1 +\frac 1 n) ^ n$ и выведите на экран их сумму.
#   Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

UserNumber = float(input('Введите число:  '))
Result = 0
SumResult = 2
while UserNumber > 1:
    Result = (1 +1/(UserNumber))**(UserNumber)
    SumResult = SumResult + Result
    UserNumber -= 1

print(UserNumber, SumResult)
