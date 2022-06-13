# -*- coding: utf-8 -*-
"""
Created on Mon May 23 17:29:46 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.01 #deltat

t = np.arange(0,500+dt,dt) #intervalo de tempo

ax = np.zeros(t.size) #acelaracao em x
vx = np.zeros(t.size) #velocidade em x
x = np.zeros(t.size) #posicao em x

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
    FRes = Cres/2*area*Par*vx[i]**2+Cyu*m*g + m*g*np.sin(np.radians(5)) +  Cyu*m*g*np.cos(np.radians(5)) #formula importante
    F = Fcic - FRes
    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    if(x[i] >= 2000):
        break;
        
        
        
t = t[:i+1]
x = x[:i+1]
ax = ax[:i+1]
vx = vx[:i+1]

print(x[-1])
print(x[-2])
tmed = t[-1]+t[-2]/2
print(tmed) #tempo que demorou mais ou menos
print(vx[-1]) #velocidade terminal
plt.plot(t,vx, label="velocity")
plt.grid()
