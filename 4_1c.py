#IMPORT
import numpy as np
import matplotlib.pyplot as plt

#INPUTS
g = 9.8

t0 = 0
tF = 1
dT = 0.01       

v0 = 100/3.6
vT = 100/3.6        #b

D = g/vT**2         #b

teta = np.radians(10)

vx0 = v0*np.cos(teta)
vy0 = v0*np.sin(teta)

y0 = 0
x0 = 0

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

vx = np.empty(N+1)
ax = np.empty(N+1)

vy = np.empty(N+1)
ay = np.empty(N+1)

y = np.empty(N+1)
x = np.empty(N+1)
v = np.empty(N+1)
Y0 = np.zeros(N+1)

vx[0] = vx0
vy[0] = vy0
y[0] = y0
x[0] = x0

#Euler
for i in range (N):
    v = np.sqrt(vx[i]**2 + vy[i]**2)     #b
    
    ay[i] = -g - D*vy[i]*v               #b
    vy[i+1] = vy[i] + ay[i]*dT
    y[i+1] = y[i] + vy[i]*dT
    
    ax[i] = 0 - D*vx[i]*v               #b
    vx[i+1] = vx[i] + ax[i]*dT
    x[i+1] = x[i] + vx[i]*dT
    
    t[i+1] = t[i] + dT


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
yT =y0 + vy0*t -(1/2)*(g)*(t**2)

#f --> yMax
ymax = np.max(y)
print("ymax = {:0.4f} m".format(ymax))

for i in range(N):
    if (v[i] < v[i+1]):
        print("ymax = {:0.2f}m --> i".format(v[y[i]]))
    break












#GRAPHS

plt.plot(x, y, "-b", label ="Com resistencia")
plt.grid()
plt.title("Trajetoria em y")
#THEORIC
plt.plot(xT, yT, "-m", label ="Sem resistencia")

plt.xlabel("x(m)")
plt.ylabel("y(m)")


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






