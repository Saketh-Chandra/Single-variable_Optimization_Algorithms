from scipy.misc import derivative
from math import sin, cos, tan, degrees, e


def f(x):
    return eval(equ_function)


def NewtonRaphsonMethod_termination(x0, ε):
    i = 0
    while (True):
        i += 1
        if (x0 < -0.01 or x0 > 0.01):
            dx = 0.01
        elif (-0.01 < x0 < 0.01):
            dx = 0.0001
        print(f'\n \nIteration -{i} --------------------------------------\n')
        f_das1 = derivative(f, x0, dx=dx)
        f_das2 = derivative(f, x0, dx=dx, n=2)
        print(f'f`= {f_das1}, f``= {f_das2}')
        x0 = x0 - (f_das1 / f_das2)
        f_das1 = derivative(f, x0, dx=dx)
        print(f'f`(x({i})) = {f_das1}')
        if (abs(f_das1) > ε):
            pass
        else:
            break
    print(f'So minimum at x({i}) = {x0})')


def NewtonRaphsonMethod_iterations(x0, Iteration):
    for i in range(1,Iteration+1):
        if (x0 < -0.01 or x0 > 0.01):
            dx = 0.01
        elif (-0.01 < x0 < 0.01):
            dx = 0.0001
        print(f'\n \nIteration - {i} --------------------------------------\n')
        f_das1 = derivative(f, x0, dx=dx)
        f_das2 = derivative(f, x0, dx=dx, n=2)
        print(f'f`= {f_das1}, f``= {f_das2}')
        x0 = x0 - (f_das1 / f_das2)
        f_das1 = derivative(f, x0, dx=dx)
        print(f'f`(x({i})) = {f_das1}')
    print(f'So minimum at x({i}) = {x0})')


def run():
    global equ_function
    equ_function = str(input("enter the function: "))
    x0 = float(input('x(0)/x'))
    choose = int(input('do you want \n1) iterations method \n2) termination parameter(𝜀)'))
    if choose == 1:
        iterations = int(input('how many iterations do you need?'))
        NewtonRaphsonMethod_iterations(x0, Iteration=iterations)
    elif choose == 2:
        ε = float(input('termination parameter'))
        NewtonRaphsonMethod_termination(x0, ε)
