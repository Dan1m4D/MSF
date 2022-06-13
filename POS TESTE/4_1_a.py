#IMPORT
import numpy as np
import matplotlib.pyplot as plt

#INPUTS
g = 9.8

t0 = 0
tF = 1
dT = 0.01       

v0 = 100/3.6

teta = np.radians(10)

vx0 = v0*np.cos(teta)
vy0 = v0*np.sin(teta)

y0 = 0
x0 = 0

#D = g/vT**2

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

vx = np.empty(N+1)
ax = np.empty(N+1)

vy = np.empty(N+1)
ay = np.empty(N+1)

y = np.empty(N+1)
x = np.empty(N+1)
Y0 = np.zeros(N+1)

vx[0] = vx0
vy[0] = vy0
y[0] = y0
x[0] = x0

#Euler
for i in range (N):
    ay[i] = -g
    vy[i+1] = vy[i] + ay[i]*dT
    y[i+1] = y[i] + vy[i]*dT
    
    ax[i] = 0
    vx[i+1] = vx[i] + ax[i]*dT
    x[i+1] = x[i] + vx[i]*dT
    
    t[i+1] = t[i] + dT
ay[N] = -g
ax[N] = 0

#PRINTS
print("VELOCITIES:\n")
print("v0y = {:0.4f} m/s".format(vy0))
print("v0x = {:0.4f} m/s".format(vx0))
print("v0 = {:0.4f} m/s".format(v0))
print("=================================\n")

print("POSITIONS:")
print("Initial:\n")
print("y0 = {:0.4f} m/s".format(vy0))
print("x0 = {:0.4f} m/s".format(vx0))
print(" = {:0.4f} m/s".format(v0))
print("---------------------------------")
print("Final:\n")
print("y0 = {:0.4f} m/s".format(vy0))
print("x0 = {:0.4f} m/s".format(vx0))
print(" = {:0.4f} m/s".format(v0))
print("=================================")

#Theoric values
xT = vx0*t + x0
yT =y0 + vy0*t -(1/2)*g*(t**2)


#GRAPHS

plt.plot(t, y, "-b", label ="Experimental (Euler)")
plt.grid()
plt.title("Trajetoria em y")
#THEORIC
plt.plot(t, yT, "-m", label ="Theoric")

plt.xlabel("x(m)")
plt.ylabel("y(m)")

#GROUND
plt.plot(t, Y0, "-g", label = "GROUND")
plt.legend()
plt.show()
"================================================"

"================================================"
plt.plot(t, vx, "-m")
plt.grid()
plt.title("Lei da velocidade em x")

plt.xlabel("t(s)")
plt.ylabel("vx(m/s)")
plt.show()
"================================================"
plt.plot(t, vy, "-b")
plt.grid()
plt.title("Lei da velocidade em y")

plt.xlabel("t(s)")
plt.ylabel("vy(m/s)")
plt.show()
"================================================"






