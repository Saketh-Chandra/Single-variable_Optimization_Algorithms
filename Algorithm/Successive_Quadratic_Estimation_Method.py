from math import sin, cos, tan, degrees


def f(x):
    return eval(equ_function)


def SuccQuadEstimation_iterations(x1, Δ, iterations):
    i = 0
    f1 = f(x1)
    x2 = x1 + Δ
    f2 = f(x2)
    if f1 >= f2:
        x3 = x1 + (2 * Δ)
    else:
        x3 = x1 - Δ
    for i in range(1, iterations + 1):
        f1 = f(x1)
        f2 = f(x2)
        f3 = f(x3)
        print(f'\niteration - {i} -------------------------')
        Fmin = min(f1, f2, f3)

        if Fmin == f1:
            xmin = x1
        elif Fmin == f2:
            xmin = x2
        else:
            xmin = x3

        print(f'(x1,x2,x3)=({x1},{x2},{x3})')
        print(f'(f1,f2,f3)=({f1},{f2},{f3})')
        print(f'Fmin={Fmin}')
        a1 = (f2 - f1) / (x2 - x1)
        a2 = (1 / (x3 - x2)) * (((f3 - f1) / (x3 - x1)) - a1)

        # print(type(a1), type(a2))
        print(f'(a1,a2)=({a1}.{a2})')
        xbar = ((x1 + x2) / 2) - (a1 / (2 * a2))

        print(f'xbar = {xbar}')
        print(f'f(xbar)={f(xbar)}')

        val = list((x1, x2, x3, xbar))
        val.sort()
        (_, x1, x2, x3) = val
    print(f'Min after {i} iterations is at {xbar}')


def SuccQuadEstimation_termination(x1, Δ, δ):
    i = 0
    f1 = f(x1)
    x2 = x1 + Δ
    f2 = f(x2)
    if f1 >= f2:
        x3 = x1 + (2 * Δ)
    else:
        x3 = x1 - Δ
    while (True):
        i += 1
        f1 = f(x1)
        f2 = f(x2)
        f3 = f(x3)
        print(f'\niteration - {i} -------------------------')
        Fmin = min(f1, f2, f3)
        print(f'Fmin={Fmin}')
        if Fmin == f1:
            xmin = x1
        elif Fmin == f2:
            xmin = x2
        else:
            xmin = x3

        print(f'(x1,x2,x3)=({x1},{x2},{x3})')
        print(f'(f1,f2,f3)=({f1},{f2},{f3})')

        a1 = (f2 - f1) / (x2 - x1)
        a2 = (1 / (x3 - x2)) * (((f3 - f1) / (x3 - x1)) - a1)

        # print(type(a1), type(a2))
        print(f'(a1,a2)=({a1}.{a2})')
        xbar = ((x1 + x2) / 2) - (a1 / (2 * a2))

        print(f'xbar = {xbar}')

        fxbar = f(xbar)
        print(f'f(xbar)={fxbar}')

        diff_Fmin_fxbar = abs(Fmin - fxbar)
        diff_xmin_xbar = abs(xmin - xbar)

        if (diff_Fmin_fxbar < δ and diff_xmin_xbar < δ):
            print(f'x={xmin} is the minimum point')
            break
        else:
            val = list((x1, x2, x3, xbar))
            val.sort()
            (_, x1, x2, x3) = val
            # print(val)
            print(f'The Best 3 points are {x1},{x2},{x3}')


def run():
    global equ_function
    equ_function = str(input("enter the function: "))
    x1 = float(input('x1 '))
    Δ = float(input('increment value(Δ)'))
    choose = int(
        input('do you want \n1) iterations of successive quadratic estimation method \n2) termination parameter'))
    if choose == 1:
        iterations = int(input('how many iterations do you need?'))
        SuccQuadEstimation_iterations(x1=x1, Δ=Δ, iterations=iterations)

    elif choose == 2:
        terminationparameter = float(input('termination parameter: '))
        SuccQuadEstimation_termination(x1=x1, Δ=Δ, δ=terminationparameter)

    else:
        print('wrong entry! ')

# equ_function = '(x**2)+(54/x)'
# SuccQuadEstimation(x1=(1), Δ=(1), δ=0.01)
#
