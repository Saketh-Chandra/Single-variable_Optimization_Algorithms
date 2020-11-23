from Algorithm import BisectionMethod, GoldenSectionSearch, NewtonRaphsonMethod, Successive_Quadratic_Estimation_Method, \
    Gradient_based_methods, ExhaustiveSearch, Bounding_Phase_Method, FibonacciSearch, Interval_Halving_Method

# BisectionMethod.run()
# GoldenSectionSearch.run()
# NewtonRaphsonMethod.run()
# Successive_Quadratic_Estimation_Method.run()
# Gradient_based_methods.run()
# ExhaustiveSearch.run()
# Bounding_Phase_Method.run()
# FibonacciSearch.run()
# Interval_Halving_Method.run()


list = [
    'Bisection Method',
    'Golden Section Search',
    'Newton Raphson Method',
    'Successive Quadratic Estimation Method',
    'Gradient Based Methods',
    'Exhaustive Search',
    'Bounding Phase Method',
    'Fibonacci Search',
    'Interval Halving Method',
    'Gradient_based_methods'
]

for i, c in enumerate(list, start=1):
    print(i, c)
choice = int(input('enter the choice'))
if choice == 1:
    BisectionMethod.run()
elif choice == 2:
    GoldenSectionSearch.run()
elif choice == 3:
    NewtonRaphsonMethod.run()
elif choice == 4:
    Successive_Quadratic_Estimation_Method.run()
elif choice == 5:
    GoldenSectionSearch.run()
elif choice == 6:
    ExhaustiveSearch.run()
elif choice == 7:
    Bounding_Phase_Method.run()
elif choice == 8:
    FibonacciSearch.run()
elif choice == 9:
    Interval_Halving_Method.run()
elif choice == 10:
    Gradient_based_methods.run()
else:
    print('wrong choice')
