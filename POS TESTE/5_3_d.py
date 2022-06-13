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

m = 0.057

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

Em = np.empty(N+1)
f = np.empty(N+1)
Wres = np.empty(N+1)

vx = np.empty(N+1)
ax = np.empty(N+1)
aresx = np.empty(N+1)

vy = np.empty(N+1)
ay = np.empty(N+1)
aresy = np.empty(N+1)


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
    v[i] = np.sqrt((vx[i]**2)+(vy[i]**2))
    
    aresx[i] = -D*abs(v[i])*vx[i]
    ax[i] = -D*abs(v[i])*vx[i]
    #ax[i] = 0
    vx[i+1] = vx[i] + ax[i]*dT
    x[i+1] = x[i] + vx[i]*dT
    
    aresy[i] = -D*abs(v[i])*vy[i]
    ay[i] = -D*abs(v[i])*vy[i] -g
    #ay[i] = -g
    vy[i+1] = vy[i] + ay[i]*dT
    y[i+1] = y[i] + vy[i]*dT
    
    t[i+1] = t[i] + dT
        
    Em[i] = (0.5*m*v[i]**2) + (m*g*y[i])
    
    #Metodo dos Trapezios
    f[i] = m*aresx[i]*vx[i] + m*aresy[i]*vy[i]
    Wres[i] = dT*((f[0]+f[i])*0.5 + np.sum(f[1:i]))
    
#Last Values   
#ax[N] = 0
#ay[N] = -g

v[N] = np.sqrt((vx[N]**2)+(vy[N]**2))
Em[N] = (0.5*m*v[N]**2) + (m*g*y[N])

ax[N] = -D*abs(vx[N])*vx[N]
ay[N] = -D*abs(vy[N])*vy[N] -g

f[N] = m*aresx[N]*vx[N] + m*aresy[N]*vy[N]
Wres[N] = dT*((f[0]+f[N])*0.5 + np.sum(f[1:N]))


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

Em00 = 0
W00 = 0
t00 = 0
Em04 = 0
W04 = 0
t04 = 0
Em08 = 0
W08 = 0
t08 = 0

for i in range(N):
    if (i == 0):
        Em00 = Em[i]
        W00 = Wres[i]
        t00 = t[i]
    if (t[i] <= 0.4 <= t[i+1]):
        Em04 = Em[i]
        W04 = Wres[i]
        t04 = t[i]
    if (t[i] <= 0.8 <= t[i+1]):
        Em08 = Em[i]
        W08 = Wres[i]
        t08 = t[i]

#PRINTS
print("VELOCITIES:\n")
print("v0x = {:0.4f} m/s".format(v0x))
print("v0y = {:0.4f} m/s".format(v0y))
print("v0 = {:0.4f} m/s".format(v0))
print("=================================")
print("POSITIONS:")
print("Initial:\n")
print("x0 = {:0.2f} m".format(x0))
print("y0 = {:0.2f} m".format(y0))
print("---------------------------------")
print("Final:\n")
print("xmax = {:0.2f} m no instante t = {:0.4f}".format(xmax, tvoo))
print("ymax = {:0.2f} m no instante t = {:0.4f}".format(ymax, tsub))
print("=================================")
print("MECHANICAL ENERGY:\n")
print("dEm = {:0.2f} - {:0.2f} = {:0.2f}J".format(Emf, Em0, dEm))
print("Em = {:0.2f}J no instante t = {:0.4f}s".format(Em00, t00))
print("Em = {:0.2f}J no instante t = {:0.4f}s".format(Em04, t04))
print("Em = {:0.2f}J no instante t = {:0.4f}s".format(Em08, t08))
print("=================================")
print("WORK OF THE RESISTIVE FORCE:")
print("Wres = {:0.2f}N no instante t = {:0.4f}s".format(W00, t00))
print("Wres = {:0.2f}N no instante t = {:0.4f}s".format(W04, t04))
print("Wres = {:0.2f}N no instante t = {:0.4f}s".format(W08, t08))
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

#POINTS
plt.plot(t00, Em00, "ok", label ="Em0.0")
plt.plot(t04, Em04, "or", label ="Em0.4")
plt.plot(t08, Em08, "ob", label ="Em0.8")

plt.xlabel("t(s)")
plt.ylabel("Em(J)")

plt.legend()
plt.show()
"================================================"
#Trabalho Resistivo
plt.plot(t, Wres, "-r", label = "Wres")
plt.grid()
plt.title("Trabalho da Forca Resistiva")

#POINTS
plt.plot(t00, W00, "ok", label ="Wres0.0")
plt.plot(t04, W04, "or", label ="Wres0.4")
plt.plot(t08, W08, "ob", label ="Wres0.8")

plt.xlabel("t(s)")
plt.ylabel("Em(J)")

plt.legend()
plt.show()
"================================================"
# plt.plot(t, vy, "-b")
# plt.grid()
# plt.title("Lei da velocidade em y")

# plt.xlabel("t(s)")
# plt.ylabel("vy(m/s)")
# plt.show()
# "================================================"