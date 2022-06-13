# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 16:16:46 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt

t0 = 0.0
tf = 3.0
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


## e)
print('Posicao em t == 2 ->>', x[t == 2])

## g) ao mudar delta_t para 0.01 a posição em t == 2 passa a ser 19.502,
##    aproximando-se do valor exato

## g) quanto menor o passo maior a exatidão do valor obtido
Exact = 1/2 * g * t**2
print(Exact[t == 2])

plt.plot(t, x, label="Método de Euler")
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (x)')
plt.title('Movimento Uniformemente Acelerado')
plt.legend()
plt.grid()
plt.show()