# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:45:52 2022

@author: Alexandre
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from numpy import block

time = np.arange(0,4,0.1)

t = sym.Symbol('t')
v = sym.Symbol('v')
vt = sym.Symbol('vt')
g = sym.Symbol('g')
D = sym.Symbol('D')
a = sym.Symbol('a')
aS = sym.Symbol('aS')


D = sym.Derivative(vt**2 / g*sym.log(sym.cosh(g/vt*t)), t, evaluate=True)
print('dy/dt=', D)

v = sym.simplify(D)
print('dy/dt=', v)

veloc = time*v
plt.plot(time, veloc)

a = sym.Derivative(D, t, evaluate=True)
print('dv/dt=', a)
aS = sym.simplify(a)
print('dy/dt=', a)