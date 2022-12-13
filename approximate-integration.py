import matplotlib.pyplot as plt
import numpy as np


def func(x):
    return 1/(9-x)


def sec_der(x):
    return 2/(9-x)**3


def max_f():
    return max(sec_der(4), sec_der(7))


def _rectangle_rule(a, b, n, frac):
    h = 1.0 * (b - a) / n
    eps = 0.05
    formula = ((24 * eps) / (max_f() * (b - a))) ** 0.5
    formula2 = (max_f()*(b-a)*h**2)/24
    print(f'h <= {formula}')
    print(f'R(f) <= {formula2}')
    print(f'h = {h}')
    sum = 0.0
    data_x = []
    data_y = []
    xstart = a + frac * h
    for i in range(n):
        sum += func(xstart + i * h)
        data_x.append(xstart + i * h)
        data_y.append(func(xstart + i * h))
        print(i, xstart + i * h, func(xstart + i * h))

    x = np.linspace(4, 7, 10)
    y = 1 / (9 - x)
    xin = data_x
    yin = data_y
    plt.plot(x, y, color='pink')
    plt.plot(xin, yin, 'x', color='cyan')
    plt.show()
    print("Розв'язок:")

    return sum * h


def midpoint_rectangle_rule(a, b, n):
    print(_rectangle_rule(a, b, n, 0.5))


midpoint_rectangle_rule(4, 7, 10)


