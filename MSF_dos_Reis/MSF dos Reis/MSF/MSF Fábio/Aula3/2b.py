import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
t = sym.Symbol('t')
v = sym.Symbol('v')
vt = sym.Symbol('vt')
g = sym.Symbol('g')
D = sym.Symbol('D')
a = sym.Symbol('a')
aS = sym.Symbol('aS')


D = sym.Derivative((v**2/g)*sym.log(sym.cosh(g*t/v)), t, evaluate=True)
print('dy/dt=', D)
v=sym.simplify(D)
print('dy/dt=', v)
a = sym.Derivative(D, t, evaluate=True)
print('dv/dt=', a)

