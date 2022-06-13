# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:14:56 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001      #intervalo de tempo
angle = np.radians(10)
g = -9.8
t = np.arange(0,3+dt, dt) #espaço de tempo
y = np.zeros(t.size)    #espaço para inserir valores de y
x = np.zeros(t.size)    #espaço para inserir valores de x
vx = np.zeros(t.size)   #espaço para inserir valores da velocidade em x
vy = np.zeros(t.size)   #espaço para inserir valores da velociadade em y
v0 = 100/3.6            # velocidade inicial

vx[0] = v0*np.cos(angle)    #velocidade segundo 0x
vy[0] = v0*np.sin(angle)    #velocidade segundo 0y

ax = 0      #acelaraçao segundo 0x
ay = g      #acelaraçao segundo 0y

for i in range(t.size-1):   #metodo de Euler para a lei da vel. e mov.
    vx[i+1] = vx[i] + ax * dt
    vy[i+1] = vy[i] + ay * dt
    x[i+1] = x[i] + vx[i] * dt
    y[i+1] = y[i]+ vy[i] * dt
    if y[i+1] < 0:
        break

t = t[:i+2]
x = x[:i+2]
y = y[:i+2]
vx = vx[:i+2]
vy = vy[:i+2]



angle1 = np.radians(10)
g1 = -9.8
t1 = np.arange(0,3+dt, dt)
y1 = np.zeros(t.size)
x1 = np.zeros(t.size)
vx1 = np.zeros(t.size)
vy1 = np.zeros(t.size)
v01 = 100/3.6

D1 = -g1/(100/3.6)**2   # D da Fres = m * D |v|**2 * v

vx1[0] = v0*np.cos(angle) #velocidade segundo 0x
vy1[0] = v0*np.sin(angle) #velocidade segundo 0y

#ax = 0
#ay = g

for i in range(t1.size-1):
    v1 = np.sqrt(vx1[i]**2 + vy1[i]**2) #modulo da velocidade
    ax1 = -D1*v1*vx1[i]                 #acelaraçao segundo 0x
    ay1 = g1-D1*v1*vy1[i]               #acelaraçao segundo 0y
    vx1[i+1] = vx1[i] + ax1 * dt        #metodo de Euler
    vy1[i+1] = vy1[i] + ay1 * dt        #...
    x1[i+1] = x1[i] + vx1[i] * dt       #...
    y1[i+1] = y1[i]+ vy1[i] * dt        #...
    if y1[i+1] < 0:
        break

t1 = t1[:i+2]
x1 = x1[:i+2]
y1 = y1[:i+2]
vx1 = vx1[:i+2]
vy1 = vy1[:i+2]


aux = np.argmin(abs(y[-2:]))    #lista com os ultimos dois valores de y
aux1 = np.argmin(abs(y1[-2:]))  #lista com os ultimos dois valores de y1
tsolosi = t[-2:][aux]           #tempo onde o y vai ser menor
tsolosi1 = t1[-2:][aux1]        #tempo onde o y1 vai ser menor
xsolosi = x[-2:][aux]           #x onde o y vai ser menor
xsolosi1 = x1[-2:][aux1]        #x onde o y1 vai ser menor
print("SEM RES | COM RES")
print("Instante de altura máxima")
print(t[np.where(y == np.amax(y))], " | ", t1[np.where(y1 == np.amax(y1))] )
print("Altura máxima")
print(np.amax(y), " | ", np.amax(y1))
print("Instante de regresso ao solo")
print(tsolosi, " | ", tsolosi1)
print("Maximo alcançe")
print(xsolosi, " | ", xsolosi1)

plt.plot(x,y, label="Sem Res")
plt.plot(x1,y1, label="Com Res")
#plt.plot(t,y,label="ty")
#plt.plot(t,x,label="tx")
plt.legend()
plt.grid()
plt.show()
