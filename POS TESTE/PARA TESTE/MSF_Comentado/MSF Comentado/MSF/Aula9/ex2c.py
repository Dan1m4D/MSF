# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:29:46 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

t = np.arange(0,200+dt,dt)

ax = np.zeros(t.size) #acelaracao em x
vx = np.zeros(t.size) # velocidade em x
x = np.zeros(t.size) # posicao em x

Cyu = 0.004 #coeficiente de resistencia de um piso liso de alcatrao
Cres = 0.9 #coeficiente de resistencia do ar
area = 0.3 #area frontal
Par = 1.225 #densidade do are
m = 75 #massa do moco
Potencia = 298.28  #converter cv para joules/s ou Watt
vx[0] = 1 #velocidade inicial
g = 9.8 #gravidade
    
for i in range(t.size-1):
    Fcic = Potencia/vx[i] #forca exercida pelo ciclista
    FRes = Cres/2*area*Par*vx[i]**2+Cyu*m*g  #forca de resistencia
    F = Fcic - FRes #soma das forcas
    ax[i] = F/m  #acelaracao e igual a forca/massa
    vx[i+1] = vx[i] + ax[i]*dt #metodo de Euler
    x[i+1] = x[i] + vx[i]*dt
    if(x[i]>=2000):
        break;
        
        
t = t[:i]
x = x[:i]
ax = ax[:i]
vx = vx[:i]

xinverted = x[-1:-50:-1] #pq raio e que isto foi feito
plt.plot(t,x, label="pos")

plt.plot(t,vx, label="velocity")
print(t[-1])
plt.grid()