from math import sin, cos, tan, degrees, e


def f(x):
    return eval(equ_function)


def ExhaustiveSearch(a, b, n):
    x1 = a
    Δx = (b - a) / n
    x2 = x1 + Δx
    x3 = x2 + Δx
    i = 1
    while (True):
        print(f'\n \nIteration -{i} --------------------------------------\n')
        i = i + 1
        (a, b, c) = (f(x1), f(x2), f(x3))
        print(f'x1 = {x1}, x2 = {x2}, x3 = {3}')
        print(f'f(x1) = {a},\nf(x2) = {b},\nf(x3) = {c}')
        if (a >= b <= c):
            print(f'the minimum point lies in ({x1},{x3})')
            break
        else:
            x1 = x2
            x2 = x3
            x3 = x2 + Δx
        if (x3 < b):
            continue
        else:
            print(f'no minimum exists in ({a},{b}) or a boundary point is the minimum point')


def run():
    global equ_function
    equ_function = str(input("enter the function: "))
    lower = float(input('lower'))
    upper = float(input('upper'))
    choose = int(input('do you want \n1) dividing the interval \n2) Bracket an interval'))
    if choose == 1:
        n = float(input('dividing the interval into (n) '))
    elif choose == 2:
        Δx2 = float(input('Bracket an interval of length ? '))
        n = 2 * (upper - lower) / Δx2
        print(n)
    ExhaustiveSearch(a=lower, b=upper, n=n)
