# -*- cd1ing: utf-8 -*-
"""
Created on Tue Apr 19 14:58:28 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.01   #deltat
m = 0.45    #massa da bola
r = 0.11    #raio da bola
area = np.pi*r**2   #are da bola
PAr = 1.225 #kg/m^3 densidade do ar
Terminalvelocity = 100*1000/3600 #m/s velocidade terminal
t = np.arange(0,0.5+dt, dt) #array dos varios intervalos de tempo
g = 9.8     #gravidade
Rx = np.zeros(t.size) #posiçao em 0x
Vx = np.zeros(t.size) #velocidade em 0x

Ry = np.zeros(t.size) #posicao em 0y
Vy = np.zeros(t.size) #velocidade em 0y
Wy = 400   #rotaçao da bola em y w(0;400;0)

Rz = np.zeros(t.size) #posico em 0z
Vz = np.zeros(t.size) #velocidade em 0z


Rz[0] = 23.8 #posicao inicial em z R(0;0;23.8)
Vx[0] = 25  #velocidade inicial V(25;5;-50)
Vy[0] = 5   #...
Vz[0] = -50 #...

D = g/(Terminalvelocity**2) #Aquele D todo manhoso da Fres
mag = 0.5*PAr*area*r #Força de Magnus sem os vetores


for i in range(0,t.size-1):
    vv=np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2)  #modulo da velocidade
    
    
    amx = mag * Wy*Vz[i]/m #acelaraçao em x aplicada pela forca de magnus
    amz = -mag * Wy*Vx[i]/m #acelaraçao em z aplicada pela forca de magnus
    amy = 0
    
    ax = -D*vv*Vx[i]+amx #acelaracao em x
    ay = -g-D*vv*Vy[i]+amy #acelaracao em y
    az = -D*vv*Vz[i]+amz #acelaracao em z
    
    Vx[i+1] = Vx[i]+ax*dt #metodo de Euler
    Vy[i+1] = Vy[i]+ay*dt
    Vz[i+1] = Vz[i]+az*dt
    
    Rx[i+1] = Rx[i] + Vx[i] * dt
    Ry[i+1] = Ry[i] + Vy[i] * dt
    Rz[i+1] = Rz[i] + Vz[i] * dt
    
plt.plot(t,Rx,label="x")
plt.plot(t,Ry,label="y")
plt.plot(t,Rz,label="z")
plt.legend()
plt.grid()

#ax = plt.axes(projection='3d')
#ax.plot3D(Rx, -Rz, Ry, 'gray')

