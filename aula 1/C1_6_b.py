# IMPORTS
import matplotlib.pyplot as plt
import numpy as np

#-----------------------------------------------------------------------------

def Reg_Linear (x,y):
    # Ver o numero de pontos dos arrays:
    npontos = x.size

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

#Arrays
X = np.array([0.00,0.735,1.363,1.739,2.805,3.814,4.458,4.955,5.666,6.329], dtype=np.float32)

#Truque para trcar variáveis (Listas) sem alterar código
x = X

# Ver o numero de pontos dos arrays:
npontos = x.size

#Array 2
T = np.arange(0,npontos,1)

#Gráfico de pontos
plt.plot(X, T, "ob")

plt.xlabel("t (s)")            #labels...
plt.ylabel("X (km)")            #labels...

m, b = Reg_Linear(T, X)



