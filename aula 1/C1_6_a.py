# IMPORTS
import matplotlib.pyplot as plt
import numpy as np

#Arrays
X = np.array([0.00,0.735,1.363,1.739,2.805,3.814,4.458,4.955,5.666,6.329], dtype=np.float32)

#Truque para trcar variáveis (Listas) sem alterar código
x = X

# Ver o numero de pontos dos arrays:
npontos = x.size

#Array 2
T = np.arange(0,npontos,1)

#Gráfico de pontos
plt.plot(X, T, "ob")

plt.xlabel("L (cm)")            #labels...
plt.ylabel("X (cm)")            #labels...