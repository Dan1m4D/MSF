# Imports
import matplotlib.pyplot as plt
import numpy as np

#INPUTS
g = 9.8

t0 = 0
tF = np.sqrt(1600/g)

dT = 0.001     
  
vT = 60
v0 = 0

y0 = 800

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)
v = np.empty(N+1)
a = np.empty(N+1)
y = np.empty(N+1)
y[0] = y0


v[0] = v0

#Euler
for i in range (N):
    v[i+1] = v[i] -g*dT
    y[i+1] = y[i] +v[i]*dT
    t[i+1] = t[i] + dT
    

#Gráficos
plt.plot(t, v, "-m")
plt.grid()
plt.title("Velocidade em fun de t")

plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.show()

plt.plot(t, y, "-m")
plt.grid()
plt.title("Velocidade em fun de t")

plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.show()

print("tF --> ", tF)
print("tF --> ", v[N])
