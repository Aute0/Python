## Задача №2: Напишите программу, которая принимает на вход число N и выдает набор
#  произведений чисел от 1 до N. 
#  Пример: - пусть N = 4, тогда[1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)

# В данном случае самым очевидным способом решения будет реализовать факториал.

print("Программа выведет набор произведений чисел от 1 до выбранного вами N")
UserNumber = int(input('Введите число N:  '))
UserList = []


def CalcFact(UserNumber):
    if UserNumber == 1:
        return 1
    else:
        return UserNumber * CalcFact(UserNumber - 1)


for i in range(1, UserNumber+1):
    UserList.append(CalcFact(i))
print(UserList)








