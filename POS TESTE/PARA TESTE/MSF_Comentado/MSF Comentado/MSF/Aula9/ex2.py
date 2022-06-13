# -*- coding: utf-8 -*-
"""
Created on Mon May 23 16:55:05 2022

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
    
plt.plot(t,vx, label="velocity")

plt.grid()

print(vx[-1]) #velocidade final
print(vx[-1]*0.9) #90% da velocidade final


vx = vx - vx[-1]*0.9 #falar com o bernardo mas tem qualquer coisa a ver com dar 0 acho eu

plt.plot(t,vx, label="velocity -90%")

for i in range(vx.size-1):
    if(vx[i] == 0):
        print(t[np.where(vx == vx[i])])
        break;
    elif(vx[i] > 0):
        t1 = t[np.where(vx == vx[i])]
        t2 = t[np.where(vx == vx[i-1])]
        tmed = (t1+t2)/2
        print(tmed)
        break;


plt.legend()
