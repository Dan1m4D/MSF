import numpy as np
import matplotlib.pyplot as plt

#b
#INPUTS
g = -9.8

t0 = 0
tF = 4
dT = 0.001      #f --> 0.01/10 = 0.001

v0 = 0

N = int((tF-t0)/dT)
print("N = ",N)

#Arrays
t = np.linspace(t0,tF, N)
v = np.empty(N)

v[0] = v0

#Euler
for i in range (N-1):
    v[i+1] = v[i] + g*dT

#Gráficos
#plt.plot(t, v, "-m", label = "v(t) em [0,4]s")
#plt.legend()
#plt.grid()

#plt.xlabel("t(s)")
#plt.ylabel("v(m/s)")

#b_2
#for i in range(N-1):
#    if (t[i]>(3-dT) and t[i+1] <(3+dT)):
#        print("dt, t, v = ", dT, t[i+1], v[i+1])
#        print("dt, t, v = ", dT, t[i], v[i])
                
#        print("v(3s) = {:0.2f} --> i+1".format(v[i+1]))
#        print("v(3s) = {:0.2f} --> i".format(v[i]))
        
        #Gráficos
#        plt.plot(t[i+1],v[i+1], "og", label="v(t) em 3s")
#        plt.legend()
#        break


#e
#Array
y = np.empty(N)

#Input
y0 = 0
y[0] = y0
for i in range (N-1):
    y[i+1] = y[i] + v[i]*dT

#Gráfico
#plt.plot(t, y, "-r", label = "y(t) em [0,4]s")
#plt.legend()
#plt.grid()
    
#plt.xlabel("t(s)")
#plt.ylabel("y(m/s)")

#c_2
#for i in range(N-1):
#    if (t[i]>(2-dT) and t[i+1] <(2+dT)):
#        print("dt, t, v = ", dT, t[i+1], y[i+1])
#        print("dt, t, v = ", dT, t[i], y[i])
                
#        print("y(2s) = {:0.2f} --> i+1".format(y[i+1]))
#        print("y(2s) = {:0.2f} --> i".format(y[i]))
        
        #Gráficos
        #plt.plot(t[i+1],y[i+1], "ob", label="y(t) em 3s")
        #plt.legend()
#        break

print("=============================")

#h
yT = (1/2)*g*2**2
print("y(2s) = ", yT)

X = [0.1, 0.01, 0.001, 0.0001]
E = np.empty(len(X))

for s in range(len(X)):
    dT = X[s]
    
    N = int((tF-t0)/dT)
    print("N = ",N)
    
    #Arrays
    t = np.linspace(t0,tF, N)
    v = np.empty(N)
    y = np.empty(N)

    v[0] = v0
    y[0] = y0
    #Euler
    for i in range (N-1):
        v[i+1] = v[i] + g*dT
        y[i+1] = y[i] + v[i]*dT
        #print(y[i+1])
    
    #Desvio
    for i in range(N-1):
        if (t[i]>(2-dT) and t[i+1] <(2+dT)):
            E[s] = abs(yT - y[i+1])
            print ("{:.5f} = |{:.5f} - {:.5f}|".format(E[s], yT, y[i+1]))
            print("-----------------------------")
            
            break

print(E)

#Gráficos
plt.plot(E, X, "-r", label = "Erro em função do dT")
plt.legend()
plt.grid()
    
plt.xlabel("dT(s)")
plt.ylabel("Erro")
    
    




