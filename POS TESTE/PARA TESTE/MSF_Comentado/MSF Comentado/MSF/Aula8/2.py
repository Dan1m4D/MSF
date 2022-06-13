# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:32:22 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.0001   #deltat
g = 9.8       #gravidade
m = 57/1000   #massa
v0 = 100/3.6  #velocidade inicial
ang0 = np.radians(10) #angulo segundo x
t = np.arange(0,15+dt, dt) #intervalo de tempo
TerminalVel = 100/3.6 #velocidade terminal

y0 = 0 
x0 = 0
vx0 = v0*np.cos(ang0) #velocidade em x
vy0 = v0*np.sin(ang0) #velocidade em y

E0 = m*(0.5*v0**2 + g*y0) #energia mecanica inicial
 
ind1, ind2 = round(0.4/dt), round(0.8/dt) #indice nos pontos 0.4 e 0.8

x = np.zeros(t.size)
y = np.zeros(t.size)    
vx = np.zeros(t.size)
vy = np.zeros(t.size)
v = np.zeros(t.size)
x[0], y[0] = x0, y0 #posicoes iniciais
v[0], vx[0], vy[0] = v0, vx0, vy0 #velocidades iniciais

D = g/TerminalVel**2 #Aquele D manhoso
f = np.zeros(t.size)

for i in range(t.size-1):
    vAbs = np.sqrt(vx[i]**2+vy[i]**2) #velocidade absoluta
    ax = -D*vx[i]*v[i]  #acelaracao em x
    ay = -D*vy[i]*v[i]
    f[i] = m*(ax*vx[i]+ay*vy[i]) # forca da resistencia

    ay = ay - g #acelaracao em y
    
    vx[i+1] = vx[i] + ax*dt
    vy[i+1] = vy[i] + ay*dt
    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    v[i+1] = np.linalg.norm((vx[i+1], vy[i+1]))
    if y[i+1] < 0:
        break;
        
    
t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]
v = v[:i+2]

fig1, ax = plt.subplots(1, 2, figsize=(13,6), layout="constrained")
EM = m*(0.5*v**2 + g*y) #energia mecanica nos varios pontos

ax[0].plot(x, y)

ax[1].plot(t, EM)
plt.show()

Wres1 = (0.5*(f[0]+f[ind1])+np.sum(f[1:ind1]))*dt
Wres2 = (0.5*(f[0]+f[ind2])+np.sum(f[1:ind2]))*dt

print(EM[0])
print(EM[ind1])
print(EM[ind2])
print(Wres1)
print(Wres2)
print(E0 + Wres1)
print(E0 + Wres2)
