import matplotlib.pyplot as plt
import numpy as np
g = 9.81
v = 6.8
t = np.linspace(0, 4, 1000)
yp = (v**2/g)*np.log10(np.cosh(g*t/v))
plt.plot(t, yp)
plt.ylabel('y(m)')
plt.xlabel('t(s)')
plt.title('Velocidade do volante')
plt.show()
