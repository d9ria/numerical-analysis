import numpy as np
import copy
"""Початкове наближення - (1, 1)"""


def func1(x, y):
    f = np.sin(x-y) - x*y + 1
    return f


def func2(x, y):
    g = x**2 - y**2 - 0.75
    return g


def matrix_F(x, y):
    b = np.zeros((2, 1))
    b[0][0] = func1(x, y)
    b[1][0] = func2(x, y)
    return b


def main_matrix():
    a = np.zeros((2, 2))
    a[0][0] = -0.5
    a[0][1] = 0.5
    a[1][0] = -0.5
    return a


def main():
    eps = 0.001
    x = [1 for k in range(0, 2)]
    x = np.matrix(x).transpose()
    MAX_ITER = 100
    n = 0
    A = main_matrix()
    while n < MAX_ITER:
        F = matrix_F(x[0], x[1])
        x_prev = copy.deepcopy(x)
        x = x_prev - A.dot(F)
        print(n, x)
        if np.linalg.norm((np.matrix(x_prev) - np.matrix(x)), ord=1) < eps:
            break
        n += 1

    res = np.array(x).reshape(-1,).tolist()

    print(f"\nEps = {eps}")
    print(A)
    print(f"Розв'язок: {res[0]}, {res[1]}")


main()
