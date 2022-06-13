#IMPORT
import numpy as np
import matplotlib.pyplot as plt

#INPUTS
g = 9.8

t0 = 0
tF = 1
dT = 0.001       

v0 = 100/3.6
vT = 100/3.6

D = g/vT**2

teta = np.radians(10)

v0x = v0*np.cos(teta)
v0y = v0*np.sin(teta)

x0 = 0
y0 = 0

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

vx = np.empty(N+1)
ax = np.empty(N+1)

vy = np.empty(N+1)
ay = np.empty(N+1)

x = np.empty(N+1)
y = np.empty(N+1)
v = np.empty(N+1)

Y0 = np.zeros(N+1)

vx[0] = v0x
vy[0] = v0y

x[0] = x0
y[0] = y0
v[0] = y0


#Euler
for i in range (N):
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)
    
    ax[i] = -D*abs(v[i])*vx[i]
    vx[i+1] = vx[i] + ax[i]*dT
    x[i+1] = x[i] + vx[i]*dT
    
    ay[i] = -g-D*abs(v[i])*vy[i]
    vy[i+1] = vy[i] + ay[i]*dT
    y[i+1] = y[i] + vy[i]*dT
    
    t[i+1] = t[i] + dT
        
ax[N] = 0
ay[N] = -g


#ALCANCE
xmax = 0
tvoo = 0
yvoo = 0

ymax = 0
tsub = 0
xsub = 0

for i in range(N):
    if (y[i+1]<y[i]):
        ymax = y[i]
        tsub = t[i]
        xsub = x[i]
        break
for i in range(N):   
    if (y[i+1]*y[i]<0):
        xmax = x[i]
        tvoo = t[i]
        yvoo = y[i]
        break


#PRINTS
print("VELOCITIES:")
print("v0x = {:0.4f} m/s".format(v0x))
print("v0y = {:0.4f} m/s".format(v0y))
print("v0 = {:0.4f} m/s".format(v0))
print("---------------------------------")
print("Final:")
print("vyF = {:0.4f} m/s".format(vy[N]))
print("vxF = {:0.4f} m/s".format(vx[N]))
print("=================================\n")
print("POSITIONS:")
print("Initial:")
print("x0 = {:0.2f} m".format(x0))
print("y0 = {:0.2f} m".format(y0))
print("---------------------------------")
print("Final:")
print("xmax = {:0.2f} m no instante t = {:0.4f}".format(xmax, tvoo))
print("ymax = {:0.2f} m no instante t = {:0.4f}".format(ymax, tsub))
print("=================================")


#GRAPHS

plt.plot(x, y, "-b", label ="Trajetoria")
plt.grid()
plt.title("Trajetoria de uma bola de tenis")

plt.xlabel("x(m)")
plt.ylabel("y(m)")

#GROUND
plt.plot(x, Y0, "-g", label = "GROUND")

,#POINTS
plt.plot(xmax, yvoo, "ok", label ="Alcance")
plt.plot(xsub, ymax, "or", label ="Altura max")

plt.legend()
plt.show()
"================================================"

# "================================================"
# plt.plot(t, y, "-m")
# plt.grid()
# plt.title("Lei do movimento")

# plt.xlabel("t(s)")
# plt.ylabel("y(m)")
# plt.show()
# "================================================"
# plt.plot(t, vy, "-r")
# plt.grid()
# plt.title("Lei da velocidade")

# plt.xlabel("t(s)")
# plt.ylabel("v(m/s)")
# plt.show()
# "================================================"
