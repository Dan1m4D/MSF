# RegressÃ£o Linear MSF C1.5

# IMPORTS
import matplotlib.pyplot as plt
import numpy as np

#VARIÁVEIS
g = 9.80

#Tempo
t0 = 0                      #Instante Inicial
tF = 4.0                    #Instante Final
deltaT = 0.01               #Passo (Intervalo de tempo a considerar)

#Calcular o nº de pontos a considerar
N = int((tF - t0)/(deltaT+0.01))       #O 0.1 acrescenta-se para ter a certeza de que o N é calculado corretamente +/- como o erro de cálculo

print(N) 

#Posição
x0 = 0                      #Posição Inicial

#Velocidade               
v0 = 0                      #Velocidade Inicial
#vX = g*t

#Criar os Arrays
X = []
t = []

t[0] = t0

#A

#Ciclo para o método de Euler
for i in range(N):
    t.append(t[i-1] + deltaT)
print (t)
    


