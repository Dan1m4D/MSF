# imports
import matplotlib.pyplot as plt
import numpy as np

def main():
    # inserir os dados de entrada
    y = np.array([0.1,1.4,1.7,6.5,7.7,10.4,19.5,26.1,26.5,45.9,52.5], dtype=np.float32)
    x = np.array([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5], dtype=np.float32)

    # mostrar o gráfico com os pontos (não é linear)
    plt.plot(x, y, 'o', color='m')
    plt.xlabel("")
    plt.ylabel("")
    plt.show()

    # transformar em log(x) e log(y)
    logx = np.log(x)
    logy = np.log(y)

    # calcular a regressão linear ()
    data = regression(logx, logy) # [m, b, r^2, deltam, deltab]

    # print m, b, r^2, deltam, deltab
    print("m={}, b={}, r^2={}, deltam={}, deltab={}".format(data[0], data[1], data[2], data[3], data[4]))

    # mostrar o gráfico com os pontos e a regressão linear
    plt.plot(logx, data[0]*logx+data[1]) # reta
    plt.scatter(logx, logy, marker='o', color='m') # pontos
    plt.xlabel("")
    plt.ylabel("")
    plt.show()

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