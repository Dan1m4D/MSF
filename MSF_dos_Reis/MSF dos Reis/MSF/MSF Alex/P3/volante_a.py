# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:28:42 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt


##ALINEA a)
t = np.linspace(0,4,100)
g = 9.8
vt = 6.80
y = ((vt**2)/2)*np.log(np.cosh(g*t/vt))

plt.plot(t,y)
plt.ylabel("y(t)")
plt.xlabel("t(s)")
plt.grid()

