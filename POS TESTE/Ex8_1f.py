# IMPORT
import numpy as np
import matplotlib.pyplot as plt

#COEFICIENTES DE FOURIER
def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf
"=============================================================================="

#INPUTS
g = 9.8

t0 = 0
tF = 400
dT = 0.001       

v0 = 0
xeq = 0
F0 = 7.5
wf = 1

b = 0.05

m = 1
k = 1

Et = 1

x0 = 0

N = int((tF-t0)/dT)

#Arrays
t = np.linspace(t0,tF, N+1)

x = np.empty(N+1)
v = np.empty(N+1)
a = np.empty(N+1)

Ep = np.empty(N+1)
Ec = np.empty(N+1)
Em = np.empty(N+1)

#X0 = np.zeros(N+1)

v[0] = v0
x[0] = x0

#Euler-CROMER
for i in range (N):   
    a[i] = -(k/m)*x[i] - (b/m)*v[i] + F0*np.cos(wf*t[i])/m
    v[i+1] = v[i] + a[i]*dT
    x[i+1] = x[i] + v[i+1]*dT
    
    Ep[i] = 0.5*k*x[i]**2
    Ec[i] = 0.5*m*v[i]*2
    Em[i] = Ec[i]+Ep[i]
    
    t[i+1] = t[i] + dT
        
#Last Values
a[i] = -(k/m)*x[N] - (b/m)*v[N] + F0*np.cos(wf*t[N])
Ep[N] = 0.5*k*x[N]**2
Ec[N] = 0.5*m*v[N]*2
Em[N] = Ec[N]+Ep[N]

#AMPLITUDE
Amp = []

tempos = []
periodos = []

for i in range(N):
    if (t[i]>200 and x[i-1] < x[i] > x[i+1] and i>0):
        Amp.append(x[i])
        tempos.append(t[i])
    
A = sum(Amp)/(len(Amp))
T = sum(periodos)/(len(periodos))

#Calculo dos coeficientes de fourier
ind = np.transpose([0 for i in range (1000)])       #ate 1000 maximos

afo = np.zeros(15)                                  #max de frequencias aceites
bfo = np.zeros(15)                                  #frequencias aceites

for i in range(N):
    if (t[i]>200 and x[i-1] < x[i] > x[i+1] and i>0):              
        countMax = countMax + 1
        ind[countMax] = int(i)
        
EXTRUDES1 =  ind[countMax]
EXTRUDES2 =  ind[countMax-1]

#Energia mecanica
dEm = Em[N]-Em[0]

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
print("x0 = {:0.2f} m".format(x0))
print("xeq = {:0.2f} m".format(xeq))
print("=================================")
print("WAVE RELATED:")
print("Amplitude:")
print("A = {:0.4f} m".format(A))
print("Periodo:")
print("T = {:0.4f} s".format(T))
print("=================================")
print("ENERGY:")
print("Mechanical:")
print("Em0 = {:0.3f} s".format(Em[0]))
print("EmF = {:0.3f} s".format(Em[N]))
print("dEm = {:0.2f} - {:0.2f} = {:0.2f}J".format(Em[N], Em[0], dEm))
print("---------------------------------")



#GRAPHS

plt.plot(t, x, "-b")
plt.grid()
plt.title("Oscilador harmonico forcado")

plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.show()
"================================================"
plt.plot(t, Em, "-m")
plt.grid()
plt.title("Variacao da Energia Mecanica")

plt.xlabel("x(m)")
plt.ylabel("Em(J)")
"================================================"
