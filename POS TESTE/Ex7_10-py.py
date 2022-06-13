#IMPORT
import numpy as np
import matplotlib.pyplot as plt

#INPUTS
g = 9.8

t0 = 0
tF = 10
dT = 0.0001          

O0 = np.degrees(1)               #radian
L = 1

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

a = np.empty(N+1)
w = np.empty(N+1)
O = np.empty(N+1)

Y0 = np.zeros(N+1)

w[0] = 0
O[0] = 1

#Euler
for i in range (N):
    
    a[i] = (-g/L)*np.sin(O[i])              
    w[i+1] = w[i] + a[i]*dT
    O[i+1] = O[i] + w[i+1]*dT
    
    t[i+1] = t[i] + dT

#T = 2*np.pi*np.sqrt(g/L)

#PRINTS
print("VELOCITIES:")
print("w0 = {:0.4f} m/s".format(w[0]))
print("=================================")
print("TIMES:")
#print("T = {:0.4f} s".format(T))
print("---------------------------------")


#GRAPHS

plt.plot(t, O, "-b")
plt.grid()
plt.title("Lei do Movimento")
#plt.plot(t, Y0, "-k", label= "Equilibrio")


plt.xlabel("t(s)")
plt.ylabel("teta(m)")


plt.legend()
plt.show()
"================================================"