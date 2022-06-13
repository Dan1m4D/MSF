
#Calcular Potência

u = 0.004
m = 75
Area = 0.3
par = 1.225
g=9.8
Cres = 0.9

v = 40/3.6
vx = 40/3.6

Fres = (Cres*Area*par*v**2*vx)/2

P = u*m*g*v + Fres

print("Potência = ", P)

