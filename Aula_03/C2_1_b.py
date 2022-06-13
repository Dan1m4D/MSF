import numpy as np
import matplotlib.pyplot as plt

#Converter km/h para m/s
def kMhtomS (x):
    return x/3.6

#Inputs
Ti = 0.0
Tf = 30.0

#Nº Pontos
N = 100

#Tempo
t = np.linspace(Ti,Tf, N)


vKM = 70.0
v = kMhtomS(vKM)

xCarro = v*t

plt.plot(t, xCarro, "-r", label = "Carro A")
plt.legend()

plt.xlabel("t (s)")            #labels...
plt.ylabel("x (m)")            #labels...

"--------------------------------------"
a = 2.0

xPolicia = 0.5*a*t**2

plt.plot(t, xPolicia, "-b",  label = "Carro Patrulha")
plt.legend()

#b

TInter = (2*v)/a

xInter = v*TInter

plt.plot (TInter, xInter, marker = "o")
print("t = {}; x = {}".format(TInter, xInter))


