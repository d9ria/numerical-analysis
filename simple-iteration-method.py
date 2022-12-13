#  Finding the root of a polynomial
#  f(x) = x^2 + sin(x) - 12x - 0.25 = 0, eps = 0.0001

import numpy as np


def f(x):
    return x**2 + np.sin(x) - 12*x - 0.25


def g(x):
    # return np.sqrt(12 + 0.25/x - np.sin(x)/x)
    return np.sqrt(12*x + 0.25 - np.sin(x))
    # return (x**2 + np.sin(x) - 0.25)/12


a0, b0 = 11, 13
x0 = 12
eps = 0.0001
delta = 1


def derivative_g(x):
    return (12 - np.cos(x))/(2*np.sqrt(12*x-np.sin(x)+0.25))


def q_calc1(a, b):
    return max(abs(derivative_g(a)), abs(derivative_g(b)))


q = q_calc1(a0, b0)  # max


def checking(x1, q11, delta1):
    print("|fi(x0) - x0| = ", abs(g(x1) - x1))
    print("(1 - q) * delta = ", (1 - q11) * delta1)
    n1 = int((np.log((abs(g(x1) - x1))/((1 - q11) * eps)))/(np.log(1/q11)) // 1)
    print(f"Апріорна оцінка = {n1}.")
    return abs(g(x1) - x1) <= (1 - q11) * delta1 and q11 < 1


print()
print("q = ", q)
print("Checking: ", checking(x0, q, delta))


def simple_iteration_method():
    x = 12
    n = 0
    print(f"{n}. x0 =", x)
    for iteration in range(1, 20):
        n += 1
        x_new = g(x)
        print(f"{n}. x =", x_new)
        if abs(x_new - x) < 0.0001:
            print("x = ", x_new)
            break
        x = x_new
    print(f"Апостеріорна оцінка: {n}")


simple_iteration_method()

# print(f"f(11)* f(13) = {f(a0)*f(b0)} < 0")







