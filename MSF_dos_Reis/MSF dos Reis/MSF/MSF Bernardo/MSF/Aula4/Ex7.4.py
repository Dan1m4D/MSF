# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:06:50 2022

@author: draki
"""

#ATENÇAO DUVIDO MUITO QUE ISTO ESTÁ CERTO, MAS FOI O QUE O PROF TEORICO DISSE PARA EU FAZER, REZAM QUE ISTO NAO CALHE NO TESTE!

import matplotlib.pyplot as plt
import numpy as np

vi = 10 # m/s
dt = 0.1
g = -9.8
T = np.arange(0,2.2+dt, dt)
v = np.zeros(T.size)
y = np.zeros(T.size)
a = np.zeros(T.size)
v[0] = 10
    
y1 = T*(10.0 - 4.9*T)

a[0] = g - (g)/(27.7778**2) # aceleraçao inicial

floor = np.zeros(T.size)


for i in range(0, T.size-1):    # metodo de euler
    a[i+1] = g*(1 - (1/(27.7778**2)) * v[i]*abs(v[i])) # aceleraçao no instante
    v[i+1] = v[i] + a[i] * dt # velocidade no instante
    y[i+1] = y[i] + v[i] * dt # posiçao no instante


fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.set_xlabel('tempo (s)')
ax.set_ylabel('X (m)')
ax.plot(T, floor, label="Y = 0")
ax.plot(T, y, label="pos")
ax.plot(T, y1, label="analitical")

plt.legend()