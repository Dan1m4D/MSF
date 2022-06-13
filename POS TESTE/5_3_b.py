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

teta = np.radians(10)

v0x = v0*np.cos(teta)
v0y = v0*np.sin(teta)

x0 = 0
y0 = 0

m = 0.057

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

Em = np.empty(N+1)

vx = np.empty(N+1)
ax = np.empty(N+1)

vy = np.empty(N+1)
ay = np.empty(N+1)

v = np.empty(N+1)
x = np.empty(N+1)
y = np.empty(N+1)

Y0 = np.zeros(N+1)

v[0] = v0
vx[0] = v0x
vy[0] = v0y

x[0] = x0
y[0] = y0


#Euler
for i in range (N): 
    #ax[i] = -D*abs(vx[i])*vx[i] + FmX
    ax[i] = 0
    vx[i+1] = vx[i] + ax[i]*dT
    x[i+1] = x[i] + vx[i]*dT
    
    #ay[i] = -D*abs(vx[i])*vy[i] -g + FmY
    ay[i] = -g
    vy[i+1] = vy[i] + ay[i]*dT
    y[i+1] = y[i] + vy[i]*dT
    
    t[i+1] = t[i] + dT
    
    v[i] = np.sqrt((vx[i]**2)+(vy[i]**2))
    
    Em[i] = (0.5*m*v[i]**2) + (m*g*y[i])
    
ax[N] = 0
ay[N] = -g

v[N] = np.sqrt((vx[N]**2)+(vy[N]**2))
Em[N] = (0.5*m*v[N]**2) + (m*g*y[N])

#ax[N] = -D*abs(vx[N])*vx[N]
#ay[N] = -D*abs(vy[N])*vy[N] -g

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
    
#Energia Mecanica
Em0 = Em[0]
Emf = Em[N]

dEm = Emf - Em0

#PRINTS
print("VELOCITIES:\n")
print("v0x = {:0.4f} m/s".format(v0x))
print("v0y = {:0.4f} m/s".format(v0y))
print("v0 = {:0.4f} m/s".format(v0))
print("=================================\n")
print("POSITIONS:")
print("Initial:\n")
print("x0 = {:0.2f} m".format(x0))
print("y0 = {:0.2f} m".format(y0))
print("---------------------------------")
print("Final:\n")
print("xmax = {:0.2f} m no instante t = {:0.4f}".format(xmax, tvoo))
print("ymax = {:0.2f} m no instante t = {:0.4f}".format(ymax, tsub))
print("\ndEm = {:0.2f} - {:0.2f} = {:0.2f}J".format(Emf, Em0, dEm))
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
#Energia Mecanica
plt.plot(t, Em, "-m", label = "Em")
plt.grid()
plt.title("Variacao da Energia mecanica")

plt.xlabel("t(s)")
plt.ylabel("Em(J)")
plt.show()
"================================================"
# plt.plot(t, vy, "-b")
# plt.grid()
# plt.title("Lei da velocidade em y")

# plt.xlabel("t(s)")
# plt.ylabel("vy(m/s)")
# plt.show()
# "================================================"