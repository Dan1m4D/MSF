import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

#Inputs
Ti = 0.0
Tf = 4.0

vT = 6.80       #Velocidade Terminal
g = -9.80       #Velocidade Terminal

#Nº Pontos
N = 100

#Tempo
t = np.linspace(Ti,Tf, N)

#lei do movimento
y = ((vT**2)/g)*np.log(np.cosh((g*t)/vT))

#GRÁFICOS
#Informações no gráfico
#plt.title("Queda de um volante em função do tempo")

#plt.xlabel("t (s)")            #labels...
#plt.ylabel("y (m)")            #labels...

#Plot do gráfico
#plt.grid()
#plt.plot(t, y, "-r", label = "Volante")
#plt.legend()

#b
#Definir variáveis no SymPy
t = sym.Symbol("t")
v = sym.Symbol("v")
vT = sym.Symbol("vT")
g = sym.Symbol("g")
D = sym.Symbol("D")

#Calcular derivadas
D = sym.Derivative(((vT**2)/g)*sym.log(sym.cosh((g*t)/vT)),t, evaluate = True)
print("dy/dt = ",D) 
v = sym.simplify(D)
print("dy/dt = ",v)

#Calcular valor v
#Valores
vT = 6.80       #Velocidade Terminal
g = -9.80       #Aceleração
t = np.linspace(Ti,Tf, N)
vel = vT*np.tanh(g*t/vT)

#GRÁFICOS
#Informações no gráfico
#plt.title("Queda de um volante em função do tempo")

#plt.xlabel("t (s)")            #labels...
#plt.ylabel("v (m/s)")            #labels...

#Plot do gráfico
#plt.grid()
#plt.plot(t, vel, "-m", label = "Volante")
#plt.legend()

#c
#Definir variáveis no SymPy
t = sym.Symbol("t")
v = sym.Symbol("v")
vT = sym.Symbol("vT")
g = sym.Symbol("g")
D = sym.Symbol("D")
a = sym.Symbol("a")
aS = sym.Symbol("aS")

#Calcular derivadas
D = sym.Derivative(vT*sym.tanh(g*t/vT),t, evaluate = True)
print("dv/dt = ",D) 
v = sym.simplify(D)
print("dv/dt = ",v)

#Calcular valor a
#Valores
vT = 6.80       #Velocidade Terminal
g = -9.80       #Aceleração
t = np.linspace(Ti,Tf, N)
acel = g/np.cosh(g*t/vT)**2

#GRÁFICOS
#Informações no gráfico
plt.title("Aceleração de um volante em função do tempo")

plt.xlabel("t (s)")            #labels...
plt.ylabel("a (m/s^2)")        #labels...

#Plot do gráfico
plt.grid()
plt.plot(t, acel, "-b", label = "Volante")
plt.legend()
