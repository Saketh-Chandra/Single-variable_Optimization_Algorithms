from math import sin, cos, tan, degrees


def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def f(x):
    if ('sin' or 'cos' or 'tan') in equ_function:
        x = degrees(x)
    return (eval(equ_function))


def Fibonacci_Search_Method(lower, upper, m, k=2):
    L = upper - lower
    F = Fibonacci
    for i in range(m - 1):
        print(f'\n Iteration – {i + 1} -----------------------')
        k += 1
        # print(F(m - k + 2 + 2), F(m + 1 + 2))
        lk = (F(m - k + 2 + 2) / F(m + 1 + 2)) * L
        print(f'L* =  {lk}')

        x1 = lower + lk
        x2 = upper - lk
        print(f'x1 = {x1}, x2 = {x2}')
        print(f'f(x1) = {f(x1)} , f(x2) = {f(x2)}')
        if f(x1) > f(x2):
            lower = x1
            print(f"(lower,upper)={lower, upper}")
        else:
            upper = x2
            print(f"(lower,upper)={lower, upper}")
    print('---------------------------------')


# def main_body():
#     global equ_function
#     #equ_function = '(x**2)+54/x'
#
#
#
# if __name__ == '__main__':
#     in_puts()


def run():
    global equ_function
    equ_function = str(input("enter the function"))
    lower = int(input('lower'))
    upper = int(input('upper'))
    m = int(input(' function evaluation(m/n)'))
    Fibonacci_Search_Method(lower=lower, upper=upper, m=m)
