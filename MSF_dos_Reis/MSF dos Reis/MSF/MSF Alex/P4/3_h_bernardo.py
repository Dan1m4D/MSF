# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 17:45:16 2022

@author: draki
h)
"""
import matplotlib.pyplot as plt
import numpy as np


xdt1 = -18.62
xdt2 = -19.502
xanalitical = -19.6

T = np.arange(0, 0.12, 0.001)
error1 = np.abs(xdt1 - xanalitical)
error2 = np.abs(xdt2 - xanalitical)
errorarry = [error2, error1]
Tarray = [0.01, 0.1]
m = (error2 - error1)/(0.01-0.1)

y = m*T
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('deltaT (s)')
ax.set_ylabel('Desvio (m)')
ax.plot(T, y, label='b forçado = 0')
ax.plot(0, 0, "bo", label='exato')
ax.plot(Tarray, errorarry, "x", label='exato')
