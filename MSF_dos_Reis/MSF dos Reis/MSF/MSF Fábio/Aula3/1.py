
import matplotlib.pyplot as plt
import numpy as np
v=70
a=2
t = np.linspace(0, 30, 100)
yc = t*(v*1000/3600)
yp = t**2*a*0.5
ti=2*(v*1000/3600)/a
xi=(v*1000/3600)*ti
plt.plot(t, yc)
plt.plot(t, yp)
plt.plot(ti, xi,"o")
plt.ylabel('x(m)')
plt.xlabel('t(s)')
plt.show()
