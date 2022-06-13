#C1.5

# IMPORTS
import matplotlib.pyplot as plt
import numpy as np

#Arrays
L = np.array([222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0], dtype=np.float32)
X = np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0], dtype=np.float32) 

#Gráficos

#lt.scatter(L,X)
#lt.xlabel("L (cm)")
#lt.ylabel("X (cm)")

x = L
y = X

#Multiplicar os Arrays
xy = x*y

x2 = pow(x,2)
y2 = pow(y,2)

#Somatórios
SumX = x.sum()
SumY = y.sum()

SumXY = xy.sum()

SumX2 = x2.sum()
SumY2 = y2.sum()

#Print das variáveis calculadas

print("x -->", x)
print("y -->", y)
print("xy -->", xy)
print("---------------------------")
print("SumX --->", SumX)
print("SumY --->" , SumY)
print("SumXY --->", SumXY)
print("SumX2 --->" , SumX2)
print("SumY2 --->", SumY2)