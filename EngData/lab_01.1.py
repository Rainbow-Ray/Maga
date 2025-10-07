
def t1():
    inp = input('Введите строку: \n').lower()
    count = {}
    for i in inp:
        if(i in count):
            count[i] +=1
        else:
            count[i] = 1
    mxC = ''
    mx = -1
    for c,n in count.items():
        if n > mx:
            mxC = c
            mx = n
    print(mxC)

def t2():
    while True:
        try:
            inp = int(input('Введите номер числа Фиббоначи:\n'))
        except:
            print("Введите целое положительное число")
        else:
            break

    n1 = 0
    n2 = 1
    res = 0
    for i in range(inp-1):
        res = n1 + n2
        n1 = n2
        n2 = res
    print(res)


def t3():
    while True:
        try:
            num = int(input('Введите целое положительное число:\n'))
        except:
            print("Введите целое положительное число")
        else:
            break

    res = 0
    while len(str(num))> 1:
        for i in str(num):
            res+=int(i)
        num = res
        res = 0
    print(num)

def t4(num):
    while True:
        try:
            num = str(int(input('Введите целое положительное количество комментариев:\n')))
        except:
            print("Введите целое положительное число")
        else:
            break

    num = str(int(num))

    if num[-1] == '1' and (int(num[-2:]) < 10 or int(num[-2:]) > 20):
        return print("комментарий")
    elif int(num[-1]) >= 2 and int(num[-1]) < 5 and (int(num[-2:]) < 10 or int(num[-2:]) > 20):
        return print("комментария")
    else:
        return print("комментариев")


