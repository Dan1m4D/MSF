
import matplotlib.pyplot as plt
import numpy as np
x = np.array([222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0])
y = np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0])
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
