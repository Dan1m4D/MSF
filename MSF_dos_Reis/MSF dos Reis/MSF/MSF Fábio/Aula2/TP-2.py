import matplotlib.pyplot as plt
import numpy as np
t0 = 0
x0 = 0
v0x = 0
g = 9.81
n=100
delta_t=0.1
t = np.linspace(0, n*delta_t, n)
xt = 1/2*(g*(t**2))
vt = g*t

plt.plot(t, xt, label='x(t)')
plt.plot(t, vt, label='v(t)')
plt.ylabel('x(m) / v(m/s)')
plt.xlabel('t(s)')
plt.title('Posição do objeto')
plt.legend()
plt.show()

