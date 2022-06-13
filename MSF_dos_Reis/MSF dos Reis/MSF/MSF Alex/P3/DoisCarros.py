# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:38:16 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt

vx0a = 70/3.6
ap = 2
vx0p = 0
tempo = np.linspace(0,30,3000)
xa = vx0a*tempo
xp = 0.5*ap*tempo**2

plt.xlabel("tempo (s)")
plt.ylabel("m (x)")
plt.plot(tempo,xa,label='Carro A')
plt.plot(tempo,xp,label='Carro Patrulha')
plt.legend()
plt.grid()

