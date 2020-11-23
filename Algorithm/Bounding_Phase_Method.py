from math import sin, cos, tan, degrees, e
from sys import exit
from prettytable import PrettyTable


#######  completed!

def f(x):
    if ('sin' or 'cos' or 'tan') in equ_function:
        x = degrees(x)
    return (eval(equ_function))


def BoundingPhaseMethod(x, Δ):
    x_arr = [x]

    a = f(x - abs(Δ))
    b = f(x)
    c = f(x + abs(Δ))

    print(f'f(x0-|Δ|) = {a},\nf(x0) = {b},\nf(x0+|Δ|) = {c}')
    if (a >= b >= c):
        Δ = abs(Δ)
    elif (a <= b <= c):
        Δ = abs(Δ) * -1
    elif (a >= b <= c):
        print(f'terminate and mention that minimum is between {x - abs(Δ)} and {x + abs(Δ)}')
    else:
        # print('Change the initial point')
        exit('Change the initial point')

    # print(a, b, c, Δ, a >= b <= c)
    k = 0
    table = PrettyTable()
    table.field_names = ['i', 'x(i)', 'f(x(i))']
    while (True):
        x1 = x_arr[k] + (2 ** k) * Δ
        # print(x1)
        x_arr.append(x1)
        fx1 = f(x_arr[k + 1])
        fx = f(x_arr[k])
        if fx1 < fx:
            k = k + 1
        else:
            # print(x_arr)
            # print(f'the minimum is between {x_arr[k - 1]} and {x_arr[k + 1]}')
            break
    for i, xval in enumerate(x_arr):
        table.add_row([i, xval, f(xval)])
        # print(f'i={i},x(i)={xval},f(x(i))={f(xval)}')
    print(table)
    print(f'the minimum is between {x_arr[k - 1]} and {x_arr[k + 1]}')


def run():
    global equ_function
    equ_function = str(input("enter the function: "))
    x = float(input('initial point (x): '))
    Δ = float(input('increment value (Δ): '))
    BoundingPhaseMethod(x, Δ)
