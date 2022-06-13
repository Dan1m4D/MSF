# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 20:00:14 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

y = np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])
x = np.linspace(0,9,len(y))
##Tmb se pode usar np.arange(0,len(y))
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

print("m +/- m_erro = {:0.8f} +/- {:0.8f}".format(m,m_erro))
print("b +/- b_erro = {:0.8f} +/- {:0.8f}".format(b,b_erro))
print("r2 = {:0.8f}".format(r2))

##Resposta: Sim, por o r2 é bem proximo de 1

##Alinea c) : Velocidade média é o declive da reta, logo vm = 0.71km/min