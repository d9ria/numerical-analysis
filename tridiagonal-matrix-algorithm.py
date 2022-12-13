import math


def tdma(a, b, c, f):
    print("1 1 0 0 0 | 1 \n1 3 2 0 0 | 1"
          " \n0 1 2 1 0 | 1 \n0 0 1 2 1 | 1 \n0 0 0 2 3 | 1\n")
    a, b, c, f = tuple(map(lambda k_list: list(map(float, k_list)), (a, b, c, f)))

    alpha = [-b[0] / c[0]]
    beta = [f[0] / c[0]]
    z = []
    n = len(f)
    x = [0]*n

    for i in range(1, n):
        alpha.append(-b[i]/(a[i]*alpha[i-1] + c[i]))
        beta.append((f[i] - a[i]*beta[i-1])/(a[i]*alpha[i-1] + c[i]))
        z.append(a[i]*alpha[i-1] + c[i])

    x[n-1] = beta[n - 1]

    for i in range(n-1, 0, -1):
        x[i - 1] = alpha[i - 1]*x[i] + beta[i - 1]
        print(x)

    detA = c[0] * (math.prod(z) * (-1)**len(z))

    print("\nDetA = ", detA)
    print("\nРозв'язок: ", x)


print("a0 = 0, b0 = 1, c0 = 1\n")

tdma([0, 1, 1, 1, 2], [1, 2, 1, 1, 0], [1, 3, 2, 2, 3], [1, 1, 1, 1, 1])



