# Анонимные функции

""" def sum(x)
    return x + 10

def sum1(x)
    return x + 22

def sum3(x)
    return x + 242

def mult(x)
    return x ** 2

def mult2(x)
    return x ** 3

def mult4(x)
    return x ** 5

sum(mult(2))
sum1(mult2(2))
sum3(mult2(2)) """

def sum(x,y):
    return x + y

def mult(x,y):
    return x * y

def calc(op,a,b):
#    print(op(a, b))
    return op(a, b)

print(calc(mult, 4, 5))