from scipy.misc import derivative
from math import sin, cos, tan, degrees, e


def f(x):
    return eval(equ_function)


def BisectionMethod_termination(upper, lower, 𝜀):
    (a, b) = (lower, upper)
    f_upper = derivative(f, b, dx=1e-6)  # dx is infinitesimal
    f_lower = derivative(f, a, dx=1e-6)
    if (f_upper > 0 and f_lower < 0):
        print(f'\n Since f’({a}) <0 and f’({b})>0 therefore, there is a minimum in ({a},{b})')
        print(f"f’({a}) = {f_lower} <0 \nf’({b}) ={f_upper} > 0")
        i = 1
        while (True):
            print(f'\niteration - {i} -------------------------')
            i += 1
            z = (a + b) / 2
            fz = derivative(f, z, dx=1e-6)
            print(f'f`(z) = {fz}')
            print(f'z = {z}')
            if (abs(fz) < 𝜀):
                print(f'Hence minimum is at {z}')
                break
            elif (fz < 0):
                a = z
            elif (fz > 0):
                b = z
            print(f'minimum is in ({a},{b}) ')
    else:
        print('Not possible')


def BisectionMethod_iterations(upper, lower, iterations):
    (a, b) = (lower, upper)
    f_upper = derivative(f, b, dx=1e-6)  # dx is infinitesimal
    f_lower = derivative(f, a, dx=1e-6)
    if (f_upper > 0 and f_lower < 0):
        print(f'Since f’({a}) <0 and f’({b})>0 therefore, there is a minimum in ({a},{b})')
        print(f"f’({a}) = {f_lower} <0 \nf’({b}) ={f_upper} > 0")
        for i in range(1, iterations + 1):
            print(f'\niteration - {i} ------------------------')
            z = (a + b) / 2
            fz = derivative(f, z, dx=1e-6)
            print(f'z = {z}')
            print(f'f`(z) = {fz}')
            if (fz < 0):
                a = z
            elif (fz > 0):
                b = z
            print(f'minimum is in ({a},{b}) ')
        print(
            f'So after {i} iterations we can say that minimum is at the mid-point of ({a}, {b}) i.e. at {(a + b) / 2}')
    else:
        print('Not possible')


def run():
    global equ_function
    equ_function = str(input("enter the function "))
    lower = float(input('lower'))
    upper = float(input('upper'))
    choose = int(input('do you want \n1) iterations method \n2) termination parameter(𝜀)'))
    if choose == 1:
        iterations = int(input('how many iterations do you need?'))
        BisectionMethod_iterations(lower=lower, upper=upper, iterations=iterations)
    elif choose == 2:
        terminationparameter = float(input('termination parameter(𝜀)?: '))
        BisectionMethod_termination(upper=upper, lower=lower, 𝜀=terminationparameter)
    else:
        print('wrong entry! ')

# equ_function = '(x**2)+54/x'
# lower = 2
# upper = 5
# 𝜀 = 0.5
# BisectionMethod(upper=upper, lower=lower, 𝜀=𝜀)
# a = derivative(f, x, dx=1e-6)  # dx is infinitesimal
# print(a)
