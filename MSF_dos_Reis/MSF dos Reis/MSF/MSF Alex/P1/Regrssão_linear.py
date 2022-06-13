# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 16:14:02 2022

@author: Alexandre
"""
import matplotlib.pyplot as plt
import numpy as np

#import scipy as stats

x = np.array([222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0])
y = np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])
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

#regressao = stats.linregress(x,y)     ##Library q faz todas as contas q aqui tivemos a fazer

xmax= np.max(x)*1.1
xmin= np.min(x)*0.9
ymax= np.max(y)*1.1
ymin= np.min(y)*0.9
x1 = np.array([xmin,xmax])
yline = m*x1+b

## para quando L=165.0cm
print('Valor de X quando L=165.0cm :', m*165+b)

fig1, ax = plt.subplots(1, 2, figsize=(21,9), layout="constrained")
ax[0].plot(x,y,"o")
ax[0].set_xlim([xmin,xmax])
ax[0].set_ylim([ymin,ymax])

ax[1].plot(x,y,"o",x1,yline)
ax[1].set_xlim([xmin,xmax])
ax[1].set_ylim([ymin,ymax])

