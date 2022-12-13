import numpy as np
from math import log


def f(x):
    return x**3 + 4*x - 6


def bisection_method(a, b, eps):
    print(f"a = {a}, b= {b}")
    n1 = int(log((b - a) / eps, 2) // 1)
    # n1 = int(log(abs(f(b) - f(a)) / eps, 2)//1)
    print(f"Апріорна оцінка = {n1}.")
    n = 0
    if f(a) * f(b) > 0:
        # end function, no root.
        print("Коренів не знайдено.")
    else:
        old_x = b
        x = (a + b) / 2.0
        print(n, x)
        while abs(old_x-x) > eps:
            if f(a) * f(x) < 0:
                b = x
                n += 1
            else:
                a = x
                n += 1
            old_x = x
            x = (a + b) / 2.0
            print(n, x)

        # print(f(x) < eps)
        print(f"Апостеріорна оцінка: {n}")



bisection_method(1, 2, 0.001)


