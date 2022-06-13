# Regressão Linear MSF C1.5

# IMPORTS
import matplotlib.pyplot as plt
import numpy as np

#Arrays
L = np.array([222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0], dtype=np.float32)
X = np.array([2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0], dtype=np.float32) 

#Truque para trcar vari�veis (Listas) sem alterar c�digo
x = L
y = X

# Ver o numero de pontos dos arrays:
npontos = x.size

#Multiplicar os Arrays
xy = x*y

x2 = pow(x,2)
y2 = pow(y,2)

#Somat�rios
SumX = x.sum()
SumY = y.sum()

SumXY = xy.sum()

SumX2 = x2.sum()
SumY2 = y2.sum()

#Print das vari�veis calculadas

print("x -->", x)
print("y -->", y)
print("xy -->", xy)
print("---------------------------")
print("SumX --->", SumX)
print("SumY --->" , SumY)
print("SumXY --->", SumXY)
print("SumX2 --->" , SumX2)
print("SumY2 --->", SumY2)

N = npontos

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
print("===========================")


#==============================================================================


#GR�FICOS
x_g = np.arange(80,240,10)      #criar pontos para o "x"

#Gr�fico de pontos
plt.plot(y, x, "ob")

plt.xlabel("L (cm)")            #labels...
plt.ylabel("X (cm)")            #labels...

#Gr�fico da regress�o linear

fun = m*x_g + b                 #criar a fun��o em ordem a "x"

plt.plot(x_g, fun, "--r")       #criar o gr�fico

plt.xlabel("L (cm)")            #labels...
plt.ylabel("X (cm)")            #labels...

#-----------------------------------------------------------------------------

def Reg_Linear (x,y):
    # Ver o numero de pontos dos arrays:
    npontos = x.size

    #Multiplicar os Arrays
    xy = x*y

    x2 = pow(x,2)
    y2 = pow(y,2)

    #Somat�rios
    SumX = x.sum()
    SumY = y.sum()

    SumXY = xy.sum()

    SumX2 = x2.sum()
    SumY2 = y2.sum()

    #Print das vari�veis calculadas

    print("x -->", x)
    print("y -->", y)
    print("xy -->", xy)
    print("---------------------------")
    print("SumX --->", SumX)
    print("SumY --->" , SumY)
    print("SumXY --->", SumXY)
    print("SumX2 --->" , SumX2)
    print("SumY2 --->", SumY2)

    N = npontos

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
    print("===========================")
    
    return m, b

#-------------------------------------------------------------------------------------











