from math import sin, cos, tan, degrees, e, log10


def f(x):
    if ('sin' or 'cos' or 'tan') in equ_function:
        x = degrees(x)
    return (eval(equ_function))


def fx(w):
    x = w * (upper - lower) + lower
    return f(x)


def GoldenSectionSearch(lower, upper, i):
    aw = (lower - lower) / (upper - lower)
    bw = (upper - lower) / (upper - lower)
    for iteration in range(i):
        print(f'\n \nIteration -{iteration + 1} --------------------------------------\n')
        lw = bw - aw
        w1 = aw + (0.618) * lw
        w2 = bw - (0.618) * lw
        print(f'w1 = {w1}  w2 = {w2}')
        a = fx(w1)
        b = fx(w2)
        print(f'f({w1}) = {a}, f({w2}) = {b}')
        if a < b:
            # print(f' Eliminate ({aw},{bw})')
            (aw, bw) = (w2, bw)
        else:
            (aw, bw) = (aw, w1)
        print(f'The new interval is (aw,bw) = ({aw},{bw})')
        print('\n---------------------------------------------------')
        # print((upper - lower), lower)
        # print(aw, bw)
        ax = (aw) * (upper - lower) + lower
        bx = (bw) * (upper - lower) + lower
        print(f'Minimum of the given function lies in ({ax},{bx})')


def run():
    global equ_function
    global lower
    global upper
    equ_function = str(input("enter the function "))
    lower = float(input('lower '))
    upper = float(input('upper '))

    i = 0
    while (True):
        s = (0.618 ** i) * (upper - lower)
        if s < 1:
            break
        i = i + 1
    # print(i)
    choice = int(input('select\n 1)using iterations \n2)using ε'))
    if choice == 1:
        ans = input(f'Do you wand custom iterations?, \nDefault is {i} type Y/N ')
        if (ans == 'N' or ans == 'n'):
            i = int(input('How many iterations do you want? '))
        GoldenSectionSearch(lower=lower, upper=upper, i=i)
    else:
        ε = float(input('ε'))
        n = (log10(ε / (upper - lower))) / (log10(0.618))
        n = int(round(n))
        print(f'ε={ε},n={n}')
        GoldenSectionSearch(lower=lower, upper=upper, i=n)
