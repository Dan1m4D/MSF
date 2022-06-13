import numpy as np
import matplotlib.pyplot as plt

#Vars
g = -9.8
ay = g       
ax = 0

y0 = 0
x0 = 0

t0 = 0
tF = 1.01

"=================================="
#v0kmh = 100       #km/h
#v0 = v0kmh*(1000/3600)         m/s
#teta = 10
#v0x = v0*np.cos(teta)
#v0y = v0*np.sin(teta)
"=================================="

v0x = 27.36
v0y = 4.82

dT = 0.01

#Expressões --> Teórico
#vx = v0x + ax*t
#vy = v0y + g*t

tsub = v0y/g                                        #Tempo até atingir o pt + alto
tvoo = 2*tsub                                       #Tempo até atingir o solo

ymax = y0 + v0y*tsub + (1/2)*g*tsub                 #Altura máxima
xmax = x0 + v0x*tvoo     # + (1/2)*ax*tvoo           #Alcance

#Arrays
N = int(abs(tF-t0)/dT)
print("N = ", N)

T = np.empty(N)
X = np.empty(N)
Y = np.empty(N)

Vx = np.empty(N)
Vy = np.empty(N)

#Posição 0 nos arrays
T[0] = t0
X[0] = x0
Y[0] = y0

Vx[0] = v0x
Vy[0] = v0y

for i in range(N-1):                                #Método de Euler
    T[i+1] = T[i] + dT
    
    Vx[i+1] = Vx[i] + ax*dT
    Vy[i+1] = Vy[i] + ay*dT
    
    Y[i+1] = Y[i] + Vy[i]*dT
    X[i+1] = X[i] + Vx[i]*dT

#Gráficos
plt.plot(X, Y, "or")
plt.grid()

plt.xlabel("x(m)")
plt.ylabel("y(m)")

#prints
print("=======================================")
print("Tempo de subida --> {:02f}s".format(tsub))
print("Tempo de voo --> {:2f}s".format(tvoo))

print("Altura máxima --> {:2f}s".format(ymax))
print("Alcance--> {:2f}s".format(xmax))





