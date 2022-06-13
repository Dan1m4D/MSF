# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 01:26:00 2022

@author: hf_co
"""

import matplotlib.pyplot as plt
import numpy as np
m = 75  #massa do moco
Cres = 0.9 
A = 0.3
p = 1.225
u = 0.004
g = 9.8
P = 0.4 * 735.4975 #converte cv para joule/s ou Watt
vi = 1 #velocidade inicial
t0 = 0
tf = 100 #tempo final
dt = 0.001 #deltat
tolerancia = 0.00001 #oq e estas tolerancia????

n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

a = np.empty(n)
v = np.empty(n)
x = np.empty(n)

a[0] = 0
v[0] = vi
x[0] = 0

for i in range(n-1):
    v[i] = np.sqrt(v[i]**2)
    a[i] = -u*g - (Cres/(2*m))*A*p*(v[i])*v[i] + P/(m*v[i]) #cortei a massa uma vez em todos
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i]*dt

    v[n-1] = np.sqrt(v[n-1]**2)

    if (v[i]-v[i-1] < tolerancia):
        vt = v[i]
        print("Velociadade Terminal = ", vt)
        break

