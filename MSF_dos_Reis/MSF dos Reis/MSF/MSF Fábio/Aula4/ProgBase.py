
import matplotlib.pyplot as plt
import numpy as np
g = 9.8
t = np.linspace(0, 4, 100)
t100 = np.linspace(0, 3, 100)
t10 = np.linspace(0, 3, 10)
vi = 0
xi = 0
yp = 1/2*(g*t**2)+(vi*t)+xi
v = (g*t)+vi
fig1, ax = plt.subplots(1, 2, figsize=(21,9), layout="constrained")

ax[0].plot(t, v, label="v(t)")

ax[1].plot(t, yp, label="y(t)")

for i in range(t100.size-1): # Método de Euler
    dt=3/t100.size    
    t[i+1]=t[i]+dt
    v[i+1]=v[i]+g*dt
    yp[i+1]=yp[i]+(v[i]*dt)
    
ax[0].plot(t, v, "+", label="v(t) / dt=3/100")

ax[1].plot(t, yp, "+", label="y(t)/dt=3/100")

ax[0].plot(3, (g*3)+vi, "o" )
ax[0].set_ylabel('v(m/s)')
ax[0].set_xlabel('t(s)')
ax[0].set_title('Velocidade do objeto')
ax[0].legend()

ax[1].set_ylabel('y(m)')
ax[1].set_xlabel('t(s)')
ax[1].set_title('Posição do objeto')
ax[1].legend()

for i in range(t10.size-1): # Método de Euler
    dt=(3/t10.size)   
    t[i+1]=t[i]+dt
    v[i+1]=v[i]+g*dt
    yp[i+1]=yp[i]+(v[i]*dt)
    
ax[0].plot(t, v, "+", label="v(t) / dt=3/10")
ax[0].legend()

ax[1].plot(t, yp, "+", label="y(t)/dt=3/10")
ax[1].legend()



