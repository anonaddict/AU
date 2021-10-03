
from sympy import init_printing
init_printing(use_latex = True)
from sympy import *

x,y,z,t= symbols("x y z t")
#insert f(x,y,...)

#funtion of any number of variables f(x,y,z)
origin = x**2-8*x+3*y**2+12*y+33

Dx = diff(origin,x)
Dy = diff(origin,y)

grad = (Dx, Dy)

print(grad)
display(grad)
