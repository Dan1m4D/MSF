# IMPORT
import numpy as np
import matplotlib.pyplot as plt

#INPUTS
g = 9.8

t0 = 0
tF = 10
dT = 0.001       

v0 = 0

x0 = 4

m = 1

k = 1

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

x = np.empty(N+1)
vx = np.empty(N+1)
ax = np.empty(N+1)

X0 = np.zeros(N+1)

vx[0] = v0
x[0] = x0



#Euler-Crommer
for i in range (N): 
    
    ax[i] = -k*x[i]
    vx[i+1] = vx[i] + ax[i]*dT
    x[i+1] = x[i] + vx[i+1]*dT
    
    t[i+1] = t[i] + dT
        

#ALCANCE
T = 0
A = 0

for i in range(N):
    if (x[i+2]==x0):
        T =               
        break
for i in range(N):   
    if (vx[i+1]*vx[i]<0):
        
        break
    
#Energia Mecanica
# Em0 = Em[0]
# Emf = Em[N]
# dEm = Emf - Em0

# Em00 = 0
# W00 = 0
# t00 = 0
# Em04 = 0
# W04 = 0
# t04 = 0
# Em08 = 0
# W08 = 0
# t08 = 0

# for i in range(N):
#     if (i == 0):
#         Em00 = Em[i]
#         W00 = Wres[i]
#         t00 = t[i]
#     if (t[i] <= 0.4 <= t[i+1]):
#         Em04 = Em[i]
#         W04 = Wres[i]
#         t04 = t[i]
#     if (t[i] <= 0.8 <= t[i+1]):
#         Em08 = Em[i]
#         W08 = Wres[i]
#         t08 = t[i]

#PRINTS
print("VELOCITIES:")
print("v0 = {:0.4f} m/s".format(v0))
print("=================================\n")
print("POSITIONS:")
print("Initial:")
print("x0 = {:0.2f} m".format(x0))
print("---------------------------------")
print("OTHERS:")
print("T = {:0.2f} s".format(T))
print("A = {:0.2f} m".format(A))
print("---------------------------------")



#GRAPHS

plt.plot(t, x, "-b", label ="Trajetoria")
plt.grid()
plt.title("Lei do Movimento (Posição)")

plt.xlabel("t(s)")
plt.ylabel("x(m)")

#EQUILIBRIUM POINT
plt.plot(t, X0, "-k", label ="Equilibrio")

plt.legend()
plt.show()
"================================================"
#VELOCIDADE
plt.plot(t, vx, "-m", label ="Trajetoria")
plt.grid()
plt.title("Lei do Movimento (Velocidade)")
#EQUILIBRIUM POINT
plt.plot(t, X0, "-k", label ="Equilibrio")

plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
"================================================"
