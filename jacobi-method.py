import copy
import numpy as np


def solution(a, b):
    count = len(b)  # количество корней

    x = [1 for k in range(0, count)]
    print("1norm:", np.linalg.norm(x, ord=np.inf))
    n = 0
    MAX_ITER = 100
    while n < MAX_ITER:

        x_prev = copy.deepcopy(x)
        for k in range(0, count):
            S = 0
            for j in range(0, count):
                if j != k:
                    S = S + a[k][j] * x[j]
            x[k] = b[k] / a[k][k] - S / a[k][k]
        # print(n, x)

        if np.linalg.norm((np.matrix(x_prev) - np.matrix(x)), ord=np.inf) < 0.001:
            break

        n += 1

    print('Кількість ітерацій: ', n)
    print("2norm:", np.linalg.norm(x, ord=np.inf))
    return x


a = [[1, 1, 0, 0, 0],
     [1, 3, 2, 0, 0],
     [0, 1, 2, 1, 0],
     [0, 0, 1, 2, 1],
     [0, 0, 0, 2, 3]]

b = [1, 1, 1, 1, 1]

condA = np.linalg.cond(np.matrix(a), p=np.inf)

print("1 1 0 0 0 | 1 \n1 3 2 0 0 | 1"
      " \n0 1 2 1 0 | 1 \n0 0 1 2 1 | 1 \n0 0 0 2 3 | 1")

print("\neps = 0.001")

print("CondA =", condA)

print("Розв'язок: ", solution(a, b))
