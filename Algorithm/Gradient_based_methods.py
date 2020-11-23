from math import sin, cos, tan, degrees
from scipy.misc import derivative


def f(x):
    return eval(equ_function)


def run():
    global equ_function
    equ_function = str(input("enter the function: "))
    iterations = int(input('how many x values '))
    for i in range(1, iterations + 1):
        x = float(input(f"for {i} (x = )"))
        if (x < -0.01 or x > 0.01):
            dx = 0.01
        elif (-0.01 < x < 0.01):
            dx = 0.0001
        fx = derivative(f, x, dx=dx)
        print(f'f`({x}) = {fx}')
        fxx = derivative(f, x, n=2, dx=dx)
        print(f'f``({x}) = {fxx}')
        print('-----------------------------')
