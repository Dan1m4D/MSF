# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:55:18 2022

@author: Alexandre
"""


import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0
tf = 4.0
x0 = 0.
v0x = 0.
g = 9.8
delta_t = 0.1
N=int((tf-t0)/delta_t)
#N = 20
print("N =", N)

t = np.linspace(t0,tf,N+1)
x = np.zeros(N+1)
vx = np.zeros(N+1)
vxExact = np.zeros(N+1)

t[0] = t0
x[0] = x0
vxExact=g*t

for i in range(N):
    vx[i+1] = vx[i] + g*delta_t
    x[i+1] = x[i] + vx[i]*delta_t


##b) Velocidade em t == 3
print('Velocidade em t == 3 ->>', vx[t == 3])

#plt.plot(t, x, label="Método de Euler")
plt.plot(t, vxExact, label="Grafico Velocidade Exata")
plt.plot(t, vx, "x", label="Grafico Velocidade pelo metodo de Euler")
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Movimento Uniformemente Acelerado')
plt.legend()
plt.grid()
plt.show()


