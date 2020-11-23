from math import sin, cos, tan, degrees, e


def f(x):
    if ('sin' or 'cos' or 'tan') in equ_function:
        x = degrees(x)
    return (eval(equ_function))


def Interval_Halving_Method_termination(a, b, ε):
    i = 1
    while (True):
        print(f'\n \nIteration -{i} --------------------------------------\n')
        i = i + 1
        xm = (a + b) / 2
        L = b - a
        fxm = f(xm)

        print(f'interval is (a, b) = ({a},{b})')
        x1 = a + L / 4
        x2 = b - L / 4
        fx1 = f(x1)
        fx2 = f(x2)

        print(f'x(m)={xm}, x1={x1},x2={x2}')
        print(f'f(x1)={fx1},f(x2)={fx2},f(xm)={fxm}')
        if (fx1 < fxm):  # step 3
            print(f'Eliminate (xm,b)=({xm},{b})')
            b = xm
            xm = x1
        else:
            if (fx2 < fxm):  # step 4
                print(f'Eliminate (a,xm) = ({a},{xm})')
                a = xm
                xm = x2
            else:
                print('Eliminate (a,x1) and (x2,b)')
                a = x1
                b = x2
        L = b - a  # step 5
        if abs(L) < ε:
            print(f'Since now |L| = {L} < ε, the minimum lies in the interval ({a},{b})')
            # print(a, b, 'br')
            break
        else:
            print(f'Minimum is in the new interval (a,b) = ({a},{b})')


def Interval_Halving_Method_iterations(a, b, iterations):
    for i in range(1, iterations + 1):
        print(f'\n \nIteration -{i} --------------------------------------\n')
        i = i + 1
        xm = (a + b) / 2
        L = b - a
        fxm = f(xm)

        print(f'interval is (a, b) = ({a},{b})')
        x1 = a + L / 4
        x2 = b - L / 4
        fx1 = f(x1)
        fx2 = f(x2)

        print(f'x(m)={xm}, x1={x1},x2={x2}')
        print(f'f(x1)={fx1},f(x2)={fx2},f(xm)={fxm}')
        if (fx1 < fxm):  # step 3
            print(f'Eliminate (xm,b)=({xm},{b})')
            b = xm
            xm = x1
        else:
            if (fx2 < fxm):  # step 4
                print(f'Eliminate (a,xm) = ({a},{xm})')
                a = xm
                xm = x2
            else:
                print('Eliminate (a,x1) and (x2,b)')
                a = x1
                b = x2
        L = b - a  # step 5

        print(f'After {iterations} iterations, the interval that contains the minimum is ({a},{b})')


def run():
    global equ_function
    equ_function = str(input("enter the function: "))
    lower = float(input('lower : '))
    upper = float(input('upper '))
    choose = int(input('do you want \n1) iterations method \n2) termination parameter(𝜀)'))
    if choose == 1:
        iterations = int(input('how many iterations do you need?'))
        Interval_Halving_Method_iterations(lower, upper, iterations)

    elif choose == 2:
        ε = float(input('termination parameter: '))
        Interval_Halving_Method_termination(lower, upper, ε)
