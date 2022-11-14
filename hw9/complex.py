def init():
    global a
    global b
    global oper
    global c
    global d
    global x
    global y 
    print('Введите выражение для вычисления без i. Где на первой и третьей позиции стоят действительные числа, а на второй и четвёртой - мнимые')
    exp = input()
    oper = 'none'
    if exp[0]=='-':
        a = -(int(exp[1])) 
        if exp[2]=='-':
            b = -(int(exp[3]))
            if exp[4]=='-':
                oper = 'min'
            elif exp[4]=='+':
                oper = 'sum'
            elif exp[4]=='/':
                oper = 'div'
            elif exp[4]=='*':
                oper = 'mult'
            if exp[5]=='-':
                c = -int(exp[6])
                print(c)
                if exp[8]=='-':
                    d = -int(exp[9])
                else:
                    d = int(exp[8])
            else:
                c = int(exp[5])
                if exp[6]=='-':
                    d = -int(exp[7])
                else:
                    d = int(exp[7])
        elif exp[2]=='+':
            b = int(exp[3])
            if exp[4]=='-':
                oper = 'min'
            elif exp[4]=='+':
                oper = 'sum'
            elif exp[4]=='/':
                oper = 'div'
            elif exp[4]=='*':
                oper = 'mult'
            if exp[5]=='-':
                c = -int(exp[6])
                print(c)
                if exp[8]=='-':
                    d = -int(exp[9])
                else:
                    d = int(exp[8])
            else:
                c = int(exp[5])
                if exp[6]=='-':
                    d = -int(exp[7])
                else:
                    d = int(exp[7])
    else:
        a = int(exp[0])
        if exp[1]=='-':
            b = -(int(exp[2]))
            if exp[3]=='-':
                oper = 'min'
            elif exp[3]=='+':
                oper = 'sum'
            elif exp[3]=='/':
                oper = 'div'
            elif exp[3]=='*':
                oper = 'mult'
            if exp[4]=='-':
                c = -int(exp[5])
                if exp[6]=='-':
                    d = -int(exp[7])
                else:
                    d = int(exp[7])
            else:
                c = int(exp[4])
                if exp[5]=='-':
                    d = -int(exp[6])
                else:
                    d = int(exp[6])
        if exp[1]=='+':
            b = int(exp[2])
            if exp[3]=='-':
                oper = 'min'
            elif exp[3]=='+':
                oper = 'sum'
            elif exp[3]=='/':
                oper = 'div'
            elif exp[3]=='*':
                oper = 'mult'
            if exp[4]=='-':
                c = -int(exp[5])
                if exp[6]=='-':
                    d = -int(exp[7])
                else:
                    d = int(exp[7])
            else:
                c = int(exp[4])
                if exp[5]=='-':
                    d = -int(exp[6])
                else:
                    d = int(exp[6])
    x = complex(a,b)
    y = complex(c,d)
def do_it(x,y, oper):
    if oper == 'sum':
        res = x+y
    elif oper == 'min':
        res = x-y
    elif oper == 'div':
        res = x/y
    elif oper == 'mult':
        res = x*y
    print(res)
    return res
init()
do_it(x,y, oper)