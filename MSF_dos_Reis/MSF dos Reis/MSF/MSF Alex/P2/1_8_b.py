# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:06:14 2022

@author: Alexandre
"""
import matplotlib.pyplot as plt
import numpy as np

T = np.array([200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1100.0])
E = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])


## b)

x = np.log(T)
y = np.log(E)
N = len(x)

xy = x*y
sumxy = xy.sum()
sumx = x.sum()
sumy = y.sum()

xx = np.square(x)
sumxx = xx.sum()
yy = np.square(y)
sumyy = yy.sum()


m = (N*sumxy - sumx*sumy)/(N*sumxx - (sumx)**2)
b = (sumxx*sumy - sumx*sumxy)/(N*sumxx - (sumx)**2)
r_num = (N * sumxy - sumx * sumy)**2
r_den  = (N * sumxx - (sumx)**2) * (N * sumyy - (sumy)**2)
r2 = r_num/r_den

m_erro = np.abs(m) * np.sqrt(((1/r2) - 1) / (N - 2))
b_erro = m_erro * np.sqrt(sumxx/N)

plt.plot(x, m*x+b)
plt.plot(x,y, "x")
plt.xlabel("log(T)")
plt.ylabel("log(E)")

# a dependencia entre a cquantidade de energia emitida e a temperatura é uma
# dependencia direta, pois o aumento da temperatura aumenta proporcionalmente
# na quantidade de energia