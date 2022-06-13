# imports
import numpy as np


def main():
    dx = 0.002  # passo
    a = 0
    b = 2

    n = np.int((b - a) / dx) + 1  # n + 1 elementos

    x = np.zeros(n + 1)
    f = np.zeros(n)

    # aproximação trapezoidal
    for i in range(n):
        x[i + 1] = x[i] + dx
        f[i] = (x[i] ** 3) / 4

    # integração trapezoidal
    i = dx * ((f[0] + f[n - 1]) * 0.5 + np.sum(f[1:n - 1]))

    print("O integral dado é {}, com dt = {}.".format(i, dx))


main()
