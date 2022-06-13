#LANÇAMENTO DE UM CORPO COM RESISTENCIA DO AR
import numpy as np
import matplotlib.pyplot as plt

#INPUTS
g = 9.8

t0 = 0
tF = 2.5
dT = 0.001       
vT = 100*1000/3600

v0 = 10
y0 = 0

D = g/vT**2

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)
v = np.empty(N+1)
a = np.empty(N+1)
y = np.empty(N+1)
Y0 = np.zeros(N+1)

v[0] = v0

#Euler
for i in range (N):
    a[i] = -D*v[i]*np.abs(v[i])-g
    v[i+1] = v[i] + a[i]*dT
    y[i+1] = y[i] + v[i]*dT
    t[i+1] = t[i] + dT
a[N] = -D*v[N]*np.abs(v[N])-g

#Gráficos
plt.plot(t, a, "-b")
plt.grid()
plt.title("Aceleração em função de t")

plt.xlabel("t(s)")
plt.ylabel("a(m/s2)")
plt.show()
"================================================"
plt.plot(t, v, "-m")
plt.grid()
plt.title("Velocidade em função de t")

plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.show()
"================================================"
plt.plot(t, y, "-r")
plt.grid()
plt.title("Posição em função de t")
plt.plot(t, Y0, "-g")

plt.xlabel("t(s)")
plt.ylabel("y(m)")

#Prints
print("N = ",N)
print("Aceleração --> ", a)

#c_2
for i in range(N):
    if (v[i]>(0-dT) and v[i+1] <(0+dT)):
        print("dt = {}s, t = {}s, v = {}m/s".format(dT, t[i+1], v[i+1]))
        print("dt = {}s, t = {}s, v = {}m/s".format(dT, t[i], v[i]))
                        
        print("y(2s) = {:0.2f}m --> i+1".format(y[i+1]))
        print("y(2s) = {:0.2f}m --> i".format(y[i]))
        
        #Gráficos
        plt.plot(t[i+1],y[i+1], "ob", label="y quando máximo")
        plt.legend()
        break
    
for i in range(N):
    if (y[i]>(0-dT) and y[i+1] <(0+dT)):
        print("dt = {}s, t = {}s, y = {}m".format(dT, t[i+1], y[i+1]))
        print("dt = {}s, t = {}s, y = {}m".format(dT, t[i], y[i]))
                        
        print("y(2s) = {:0.2f} --> i+1".format(y[i+1]))
        print("y(2s) = {:0.2f} --> i".format(y[i]))
        
        #Gráficos
        plt.plot(t[i+1],y[i+1], "o", label="y quando volta à posição inicial")
        plt.legend()
        break
