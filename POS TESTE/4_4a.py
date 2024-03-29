#IMPORT
import numpy as np
import matplotlib.pyplot as plt

#INPUTS
g = 9.8

t0 = 0
tF = 1.5
dT = 0.001       

v0 = 130/3.6
vT = 100/3.6

teta = np.radians(10)

v0x = v0*np.cos(teta)
v0y = v0*np.sin(teta)
v0z = 0

dbola = 0.067

x0 = -10
y0 = 1
z0 = 0

D = g/vT**2

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

vx = np.empty(N+1)
ax = np.empty(N+1)

vy = np.empty(N+1)
ay = np.empty(N+1)

vz = np.empty(N+1)
az = np.empty(N+1)

x = np.empty(N+1)
y = np.empty(N+1)
z = np.empty(N+1)

Y0 = np.zeros(N+1)

vx[0] = v0x
vy[0] = v0y
vz[0] = v0z

x[0] = x0
y[0] = y0
z[0] = z0

#Euler
for i in range (N):
    ax[i] = -D*abs(vx[i])*vx[i]
    vx[i+1] = vx[i] + ax[i]*dT
    x[i+1] = x[i] + vx[i]*dT
    
    ay[i] = -D*abs(vx[i])*vy[i] -g
    vy[i+1] = vy[i] + ay[i]*dT
    y[i+1] = y[i] + vy[i]*dT
    
    az[i] = 0
    vz[i+1] = vz[i] + az[i]*dT
    z[i+1] = z[i] + vz[i]*dT
    
    t[i+1] = t[i] + dT
ax[N] = -D*abs(vx[N])*vx[N]
ay[N] = -D*abs(vy[N])*vy[N] -g

#ALCANCE
xmax = 0
tvoo = 0
yvoo = 0

ymax = 0
tsub = 0
xsub = 0

zmax = 0

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
print("VELOCITIES:\n")
print("v0x = {:0.4f} m/s".format(v0x))
print("v0y = {:0.4f} m/s".format(v0y))
print("v0z = {:0.4f} m/s".format(v0z))
print("v0 = {:0.4f} m/s".format(v0))
print("=================================\n")

print("POSITIONS:")
print("Initial:\n")
print("x0 = {:0.2f} m".format(x0))
print("y0 = {:0.2f} m".format(y0))
print("z0 = {:0.2f} m".format(z0))
print("---------------------------------")
print("Final:\n")
print("xmax = {:0.2f} m no instante t = {:0.4f}".format(xmax, tvoo))
print("ymax = {:0.2f} m no instante t = {:0.4f}".format(ymax, tsub))
print("zmax = {:0.4f} m".format(v0z))
print("=================================")

#Theoric values
xT = v0x*t + x0
yT =y0 + v0y*t -(1/2)*g*(t**2)


#GRAPHS

plt.plot(x, y, "-b", label ="Trajetoria")
plt.grid()
plt.title("Trajetoria de uma bola de tenis")
#THEORIC
#plt.plot(t, yT, "-m", label ="Theoric")

plt.xlabel("x(m)")
plt.ylabel("y(m)")

#GROUND
plt.plot(x, Y0, "-g", label = "GROUND")

#POINTS
plt.plot(xmax, yvoo, "ok", label ="Alcance")
plt.plot(xsub, ymax, "or", label ="Altura max")

plt.legend()
plt.show()
"================================================"

# "================================================"
# plt.plot(t, vx, "-m")
# plt.grid()
# plt.title("Lei da velocidade em x")

# plt.xlabel("t(s)")
# plt.ylabel("vx(m/s)")
# plt.show()
# "================================================"
# plt.plot(t, vy, "-b")
# plt.grid()
# plt.title("Lei da velocidade em y")

# plt.xlabel("t(s)")
# plt.ylabel("vy(m/s)")
# plt.show()
# "================================================"


