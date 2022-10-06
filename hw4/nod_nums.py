## Задача №2: Задайте натуральное число N. Напишите программу,
#  которая составит список простых множителей числа N.

print("Программа выведет все простые множители выбранного вами числа")
user_num = int(input('Введите ваше число: '))


def nod_nums(user_num):
   i = 2
   user_nod = []
   while i * i <= user_num:
       while user_num % i == 0:
           user_nod.append(i)
           user_num = user_num / i
       i = i + 1
   if user_num > 1:
       user_nod.append(user_num)
   return user_nod

user_nod = nod_nums(user_num)
print('{} = {}' .format(user_num, user_nod))
