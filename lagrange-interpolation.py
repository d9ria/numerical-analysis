import numpy as np
import matplotlib.pyplot as plt


def lagrange(data_x, data_y, x):
    y_ans = 0

    for i in range(data_x.size):
        p = data_y[0][i]
        for j in range(data_x.size):
            if i != j:
                p *= ((x - data_x[0][j]) / (data_x[0][i] - data_x[0][j]))
        y_ans += p
    return y_ans


def f(x):
    y = x**3
    return y


def data1():
    """ Рівновіддалені вузли """
    n = 12  # number of points
    a, b = -1, 1
    h = (b-a)/n
    data_x = np.zeros((1, n))
    data_y = np.zeros((1, n))
    x = 0.5
    for k in range(n):
        data_x[0][k] = a+h*k
        data_y[0][k] = f(data_x[0][k])
    return [data_x, data_y, x]


def data2():
    """Нулі полінома Чебишова"""
    n = 12
    data_x1 = np.zeros((1, n))
    data_y1 = np.zeros((1, n))
    x = 0.5
    k = 0
    while k <= 11:
        data_x1[0][k] = np.cos(((2*k+1)*np.pi)/(2*n))
        data_y1[0][k] = f(data_x1[0][k])
        k += 1
    return data_x1, data_y1, x


def test_lagrange():
    data_x, data_y, x1 = data1()
    y_ans = lagrange(data_x, data_y, x1)
    print(data_x)
    print(data_y)
    print("Using Lagrange Method:")
    print("F({}) = {}".format(x1, y_ans))


def test_lagrange1():
    data_x1, data_y1, x1 = data2()
    y_ans = lagrange(data_x1, data_y1, x1)
    print(data_x1)
    print(data_y1)
    print("Using Lagrange Method:")
    print("F({}) = {}".format(x1, y_ans))


test_lagrange()

test_lagrange1()

data_x, data_y, x1 = data1()
data_x1, data_y1, x2 = data2()
x = np.linspace(-1, 1, 100)
y = x**3
xin = data_x[0]
yin = data_y[0]
xin1 = data_x1[0]
yin1 = data_y1[0]
plt.plot(x, y)
plt.plot(xin, yin, '-o')
plt.plot(xin1, yin1, '-x', color='red')
plt.show()

