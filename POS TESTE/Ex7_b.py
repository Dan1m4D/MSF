# IMPORT
import numpy as np
import matplotlib.pyplot as plt

#INPUTS
g = 9.8

t0 = 0
tF = 200
dT = 0.001       

v0 = 0
x0 = 4

m = 1
k = 1

w2 = k/m

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

x = np.empty(N+1)
vx = np.empty(N+1)
ax = np.empty(N+1)

X0 = np.zeros(N+1)

vx[0] = v0
x[0] = x0



#Euler-CROMER
for i in range (N):   
    ax[i] = -w2*x[i]
    vx[i+1] = vx[i] + ax[i]*dT
    x[i+1] = x[i] + vx[i+1]*dT
    
    t[i+1] = t[i] + dT
    
    
#AMPLITUDE
Amp = []

tempos = []
periodos = []

for i in range(N):
    if (x[i-1] < x[i] > x[i+1] and i>0):
        Amp.append(x[i])
        
        tempos.append(t[i])

for i in range(1,len(tempos)-1):
    periodos.append(tempos[i+1]-tempos[i])
    
A = sum(Amp)/(len(Amp))
T = sum(periodos)/(len(periodos))

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
print("x0 = {:0.4f} m".format(x0))
print("=================================")
print("WAVE RELATED:")
print("Amplitude:")
print("A = {:0.4f} m".format(A))
print("Periodo:")
print("T = {:0.4f} s".format(T))
print("=================================")


#GRAPHS

plt.plot(t, x, "-b")
plt.grid()
plt.title("Lei do Movimento")

plt.xlabel("t(s)")
plt.ylabel("x(m)")

#EQUILIBRIUM POINT
plt.plot(t, X0, "-k", label ="Equilibrio")

plt.legend()
plt.show()
"================================================"