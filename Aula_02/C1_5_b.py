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

#rint("x -->", x)
#rint("y -->", y)
#rint("xy -->", xy)
#rint("---------------------------")
#rint("SumX --->", SumX)
#rint("SumY --->" , SumY)
#rint("SumXY --->", SumXY)
#rint("SumX2 --->" , SumX2)
#rint("SumY2 --->", SumY2)

# Ver o numero de pontos dos arrays:
N = x.size

#Calcular o r
rN = (N*SumXY - SumX*SumY)**2
rD = (N*SumX2 - pow(SumX,2))*(N*SumY2 - pow(SumY, 2))

r2 = rN/rD
r = np.sqrt(r2)

#Calcular m e deltaM
m = (N*SumXY - SumX*SumY)/(N*SumX2 - pow(SumX,2))
deltaM = abs(m)*np.sqrt((1/r2 - 1)/(N-2))

#Calcular b e deltaB
b = (SumX2*SumY - SumX*SumXY)/(N*SumX2 - pow(SumX,2))
deltaB = deltaM*np.sqrt(SumX2/N)

#Print do mx + b
print("---------------------------")
print("mx + b = ({:2f}+/-{:2f})x + ({:2f}+/-{:2f})".format(m, deltaM, b, deltaB))
print("r2 = {:2f}".format(r2))