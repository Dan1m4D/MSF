
import matplotlib.pyplot as plt
import numpy as np
E = np.array([200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100])
T = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])
x=np.log(T)
y=np.log(E)
xy=x*y
xx=np.square(x)
yy=np.square(y)

Sum_x=np.sum(x)
Sum_y=np.sum(y)
Sum_xy=np.sum(xy)
Sum_xx=np.sum(xx)
Sum_yy=np.sum(yy)
n=len(x)



    

m = (n*Sum_xy-Sum_x*Sum_y)/(n*Sum_xx-Sum_x*Sum_x)
b = (Sum_xx*Sum_y-Sum_x*Sum_xy)/(n*Sum_xx-Sum_x*Sum_x)
r2 = np.square(n*Sum_xy-Sum_x*Sum_y)/((n*Sum_xx-Sum_x*Sum_x)*(n*Sum_yy-Sum_y*Sum_y))
r = np.sqrt(r2)
delta_m = np.abs(m)*np.sqrt((1/r2-1)/(n-2))
delta_b = delta_m*np.sqrt(Sum_xx/n)


xmax = np.max(x)*1.1
xmin = np.min(x)*0.9
ymax = np.max(y)*1.1
ymin = np.min(y)*0.9
x1 = np.array([xmin,xmax])
yline = m*x1+b

fig1, ax = plt.subplots(1, 2, figsize=(21,9), layout="constrained")
ax[0].plot(x,y,"o")
ax[0].set_xlim([xmin,xmax])
ax[0].set_ylim([ymin,ymax])

ax[1].plot(x,y,"o",x1,yline)
ax[1].set_xlim([xmin,xmax])
ax[1].set_ylim([ymin,ymax])
