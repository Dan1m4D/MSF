# Imports
import matplotlib.pyplot as plt
import numpy as np

#INPUTS
g = 9.8

t0 = 0
tP = 10
tF = np.sqrt(1600/g)

dT = 0.001     
  
vTL = 60
vTP = 5
v0 = 0

DL = g/vTL**2
DP = g/vTP**2

y0 = 800

NL = int((tP-t0)/dT)

#Arrays
tL = np.linspace(t0,tF, NL+1)
vL = np.empty(NL+1)
aL = np.empty(NL+1)
yL = np.empty(NL+1)
yL[0] = y0


vL[0] = v0

#Euler
for i in range (NL):
    aL[i] = -DL*vL[i]*np.abs(vL[i])-g
    vL[i+1] = vL[i] + aL[i]*dT
    yL[i+1] = yL[i] +vL[i]*dT
    tL[i+1] = tL[i] + dT
aL[NL] = -DL*vL[NL]*np.abs(vL[NL])-g

#GrÃ¡ficos
plt.plot(tL, aL, "-b")
plt.grid()
plt.title("AceleraÃ§Ã£o em funÃ§Ã£o de t")

plt.xlabel("t(s)")
plt.ylabel("a(m/s2)")
plt.show()
"================================================"
plt.plot(tL, vL, "-m")
plt.grid()
plt.title("Velocidade em funÃ§Ã£o de t")

plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.show()
"================================================"
plt.plot(tL, yL, "-r")
plt.grid()
plt.title("PosiÃ§Ã£o em funÃ§Ã£o de t")

plt.xlabel("t(s)")
plt.ylabel("y(m)")
plt.show()

#Prints
print("N = ",NL)
print("AceleraÃ§Ã£o --> ", aL)

print("tF --> ", tF)
print("vF --> ", vL[NL])

#dps de 10s
y0 = 450

tF = np.sqrt(750/(DP*25 - g))

NL = int((tF-tP)/dT)

#Arrays
tL = np.linspace(t0,tF, NL+1)
vL = np.empty(NL+1)
aL = np.empty(NL+1)
yL = np.empty(NL+1)
yL[0] = y0


vL[0] = v0

DL = DP

#Euler
for i in range (NL):
    aL[i] = -DL*vL[i]*np.abs(vL[i])-g
    vL[i+1] = vL[i] + aL[i]*dT
    yL[i+1] = yL[i] +vL[i]*dT
    tL[i+1] = tL[i] + dT
aL[NL] = -DL*vL[NL]*np.abs(vL[NL])-g

#GrÃ¡ficos
plt.plot(tL, aL, "-b")
plt.grid()
plt.title("AceleraÃ§Ã£o em funÃ§Ã£o de t")

plt.xlabel("t(s)")
plt.ylabel("a(m/s2)")
plt.show()
"================================================"
plt.plot(tL, vL, "-m")
plt.grid()
plt.title("Velocidade em funÃ§Ã£o de t")

plt.xlabel("t(s)")
plt.ylabel("v(m/s)")
plt.show()
"================================================"
plt.plot(tL, yL, "-r")
plt.grid()
plt.title("PosiÃ§Ã£o em funÃ§Ã£o de t")


plt.xlabel("t(s)")
plt.ylabel("y(m)")

#Prints

print("tF --> ", tF)
print("vF --> ", vL[NL])
