# IMPORT
import numpy as np
import matplotlib.pyplot as plt

#INPUTS
g = 9.8

t0 = 0
tF = 1
dT = 0.001       

v0 = 0
xeq = 1.5

m = 1
k = 1

Et = 1

#Calculo do x0
x0 = np.sqrt(np.sqrt((Et/k))+xeq**2)

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

x = np.empty(N+1)
v = np.empty(N+1)
a = np.empty(N+1)

Ep = np.empty(N+1)
Ec = np.empty(N+1)
Em = np.empty(N+1)

#X0 = np.zeros(N+1)

v[0] = v0
x[0] = x0



#Euler-CROMER
for i in range (N):   
    a[i] = -2*(k/m)*(x[i]**2 - xeq**2)*x[i]
    v[i+1] = v[i] + a[i]*dT
    x[i+1] = x[i] + v[i+1]*dT
    
    Ep[i] = 0.5*k*(x[i]**2 - xeq**2)**2
    Ec[i] = 0.5*m*v[i]*2
    Em[i] = Ec[i]+Ep[i]
    
    t[i+1] = t[i] + dT
        
#Last Values
a[N] = -2*(k/m)*x[N]*(x[N]**2 - xeq**2)**2
Ep[N] = 0.5*k*(x[N]**2 - xeq**2)**2
Ec[N] = 0.5*m*v[N]*2
Em[N] = Ec[N]+Ep[N]

#PRINTS
print("TIME VARIABLES:")
print("---------------------------------")
print("t0 = {:0.3f} s".format(t0))
print("tF = {:0.3f} s".format(tF))
print("dT = {:0.3f} s".format(dT))
print("=================================")
print("VELOCITIES:")
print("Initial:")
print("v0 = {:0.4f} m/s".format(v0))
print("=================================")
print("POSITIONS:")
print("Initial:")
print("x0 = {:0.2f} m".format(x0))
print("xeq = {:0.2f} m".format(xeq))
print("=================================")
print("ENERGY:")
print("Mechanical:")
print("Em = {:0.2f} m".format(Et))
print("---------------------------------")



#GRAPHS

plt.plot(x, Ep, "-b")
plt.grid()
plt.title("Variacao da Energia Potencial")

plt.xlabel("x(m)")
plt.ylabel("Ep(J)")
plt.show()
"================================================"
plt.plot(x, Em, "-m")
plt.grid()
plt.title("Variacao da Energia Mecanica")

plt.xlabel("x(m)")
plt.ylabel("Em(J)")
"================================================"
