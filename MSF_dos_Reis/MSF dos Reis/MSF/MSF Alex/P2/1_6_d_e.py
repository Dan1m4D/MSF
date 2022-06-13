# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 21:02:49 2022

@author: Alexandre
"""

import matplotlib.pyplot as plt
import numpy as np

y = np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])
x = np.linspace(0,9,len(y))

z = np.polyfit (x,y,1)
print(z)

m = z[0]
b = z[1]

plt.plot(x,y,"o")
plt.plot(x, m*x+b)
plt.xlabel("t(min)")
plt.ylabel("d(km)")

#Sim o declive e coordenada da origem coincidem com os valores calculados na alinea b)

#e) Apresente a velocidade em km/hora
v= m*60
print("velocidade é {:.0f}km/h".format(v))