# -*- coding: utf-8 -*-
"""
Created on Tue May 31 01:44:12 2022

@author: hf_co
"""

import matplotlib.pyplot as plt
import numpy as np

k = 1
m = 1
w = np.sqrt(k/m)
g = 9.8
fi = 0
A = 4

dt = 0.01
t = np.arange(0, 10.0, dt)

va = -A*w*np.sin(w*t+fi)



vy = np.zeros(t.size)
ay = np.zeros(t.size)
vy[0] = 0
ay[0] = -A*(w**2)*np.cos(w*0 + fi)

for i in range(t.size-1): # Método de Euler-Cromer 
    ay[i+1] = -A*(w**2)*np.cos(w*t[i] + fi)   
    vy[i+1] = vy[i] + ay[i+1]*dt
plt.ylabel("velocidade (m/s)")
plt.xlabel("tempo (s)")       
plt.grid()
plt.plot(t, vy,marker="+", label="euler-cromer")
plt.plot(t, va, label="analitico")
plt.plot(t, np.zeros(t.size))
plt.legend()