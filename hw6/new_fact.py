# 15. Написать программу получающую набор произведений чисел от 1 до N.

from itertools import accumulate
import operator

N = int(input('Введите число: '))

def get_mult(N):
    return list(accumulate([x for x in range(1, N + 1)], operator.mul))


print(get_mult(N))

# Предыдущий вариант решения
#   print("Программа выведет набор произведений чисел от 1 до выбранного вами N")
#   UserNumber = int(input('Введите число N:  '))
#   UserList = []
#   def CalcFact(UserNumber):
#       if UserNumber == 1:
#           return 1
#       else:
#           return UserNumber * CalcFact(UserNumber - 1)
#   for i in range(1, UserNumber+1):
#       UserList.append(CalcFact(i))
#   print(UserList)
