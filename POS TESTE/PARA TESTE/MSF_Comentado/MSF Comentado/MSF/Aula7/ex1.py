import matplotlib.pyplot as plt
import numpy as np

dt = 0.01 #deltat
m = 57/1000 #massa da bola
r = 67/2000 #raio da bola
area = np.pi*r**2 #area da bola
PAr = 1.225 #densidade do ar
TerminalVel = 100*1000/3600 #velocidade terminal
t = np.arange(0,5+dt, dt) #intervalo de tempo
g = -9.8 #gravidade
ang0 = np.radians(10) #angulo segundo 0x
v0 = 130*1000/3600 #velocidade inicial

D = -g /TerminalVel**2 #aquele D todo estranho para a força de magnus
CMag = 0.5*PAr*r*area #Fmagnus = C * W * V

Rx = np.zeros(t.size) #posicao segundo x
Ry = np.zeros(t.size) #posicao segundo y
Rz = np.zeros(t.size) #posicao segundo z

Rx[0] = -10 #posicao inicial em x
Ry[0] = 1 #posicao inicial em y



Vx = np.zeros(t.size) #velocidade segundo x
Vy = np.zeros(t.size) #velocidade segundo y
Vz = np.zeros(t.size) #velocidade segundo z

Vx[0] = v0*np.cos(ang0) #velocidade inicial em x
Vy[0] = v0*np.sin(ang0) #velocidade inicial em x
Vz[0] = 0.0

for i in range(t.size-1):
    vAbs = np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2) #velocidade absoluta
    
    Ax = -D*vAbs*Vx[i] #acelaracao segundo x
    Ay =  g -D*vAbs*Vy[i] #acelaracao segundo y
    Az =  -D*vAbs*Vz[i] #acelaracao segundo z
    
    Vx[i+1] = Vx[i]+ Ax*dt #Euler
    Vy[i+1] = Vy[i]+ Ay*dt
    Vz[i+1] = Vz[i]+ Az*dt
    
    Rx[i+1] = Rx[i] + Vx[i]*dt
    Ry[i+1] = Ry[i] + Vy[i]*dt
    Rz[i+1] = Rz[i] + Vz[i]*dt
    
    if(Ry[i] < 0):
        break;

t = t[:i+2]
Rx = Rx[:i+2]
Ry = Ry[:i+2]
Rz = Rz[:i+2]
Vx = Vx[:i+2]
Vy = Vy[:i+2]
Vz = Vz[:i+2]

#plt.plot(t,Rx, label="X")
#plt.plot(t,Ry, label="Y")
#plt.plot(t,Rz, label="Z")
plt.plot(Rx,Ry)
plt.legend()
plt.grid()
plt.show()

aux = np.argmin(abs(Ry[-2:]))
tsolosi = t[-2:][aux]
xsolosi = Rx[-2:][aux]

print("SEM RES")
print("Instante de altura máxima")
print(t[np.where(Ry == np.amax(Ry))])
print("Altura máxima")
print(np.amax(Ry))
print("Instante de regresso ao solo")
print(tsolosi)
print("Maximo alcançe")
print(xsolosi)