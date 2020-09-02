from scipy.integrate import odeint
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from sympy.interactive import printing
import sympy as sym


M_kg=1.
f_hz=1.
Ep=0.2

w= 2*np.pi*f_hz
k= M_kg*w**2
c=2*Ep*w*M_kg





# Tranformamos la variable x' en v y x'' en v'
def OS_Ar( y, t):
    (x,v)= y 
    return (v, -(k/M_kg)*x - (c/M_kg)*v)


t = np.linspace(0, 4., 100)
X_0=(1,1)

sol=odeint( OS_Ar,X_0,t)


pos=[]
for i in sol:
    pos.append(i[0])


plt.plot(t,pos,color="b")


plt.plot()



"""
x = sym.Symbol('x') 
y = sym.Function('y')

F= y(x).diff(x,x)* M_kg+ y(x).diff(x)*c + y(x)*k

ics = {y(0): 1, y(x).diff(x).subs(x,0): 1}

a=sym.dsolve(F, ics)
"""




