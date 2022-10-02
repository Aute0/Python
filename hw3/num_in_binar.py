## Задача №4: Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:   - 45 -> 101101
#           - 3  -> 11
#           - 2  -> 10

print('Программа переводит вещественное число в двоичное')
user_num = int(input('Введите число:  '))

def binary(user_num):
    binary_num = ''
    while user_num > 0:
        binary_num = str(user_num % 2) + binary_num
        user_num //= 2
    return binary_num


binary_num = binary(user_num)
print(f'Ваше число в двоичной системе исчисления равно: {binary_num}')


