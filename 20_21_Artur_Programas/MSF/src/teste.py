# imports
import matplotlib.pyplot as plt
import numpy as np

def main():
    # inserir os dados de entrada
    x = np.array([.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
    y = np.array([.121, .997, 2.55, 6.09, 9.31, 15.8, 17.1, 25.5, 26.5, 38.8, 41.9])

    # calcular a regressão linear ()
    data = regression(x, y) # [m, b, r^2, deltam, deltab]

    # mostrar o gráfico com os pontos (não é linear)
    plt.plot(x, data[0]*x+data[1]) # reta
    plt.scatter(x, y, 'o', color='m') # pontos
    plt.xlabel("t(s)")
    plt.ylabel("x(m)")
    plt.show()

    # print m, b, r^2, deltam, deltab
    print("m={}, b={}, r^2={}, deltam={}, deltab={}".format(data[0], data[1], data[2], data[3], data[4]))


def regression(x, y):
    n = len(x) # número de medições

    # obter os somatórios necessários
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.sum(x**2)
    sum_yy = np.sum(y**2)
    sum_xy = np.sum(np.multiply(x, y))

    # calcular m, b, r^2, deltam, deltab

    m = (n*sum_xy - sum_x*sum_y)/(n*sum_xx - sum_x**2)
    b = (sum_xx*sum_y - sum_x*sum_xy)/(n*sum_xx - sum_x**2)
    rr = (n*sum_xy - sum_x*sum_y)**2/((n*sum_xx - sum_x**2)*(n*sum_yy - sum_y**2))
    deltam = np.abs(m)*np.sqrt(((1/rr)-1)/(n-2))
    deltab = deltam*np.sqrt(sum_xx/n)

    return m, b, rr, deltam, deltab

main()