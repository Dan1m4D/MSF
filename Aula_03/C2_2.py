import numpy as np
import matplotlib.pyplot as plt

#Inputs
Ti = 0.0
Tf = 4.0

vT = 6.80
g = -9.80

#Nº Pontos
N = 100

#Tempo
t = np.linspace(Ti,Tf, N)

#lei do movimento
y = ((vT**2)/g)*np.log(np.cosh((g*t)/vT))

#GRÁFICOS
#Informações no gráfico
plt.title("Velocidade de queda de um volante em função do tempo")

plt.xlabel("t (s)")            #labels...
plt.ylabel("y (m)")            #labels...


plt.grid()
plt.plot(t, y, "-r", label = "Volante")
plt.legend()


