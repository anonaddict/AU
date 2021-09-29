
from sympy import init_printing
init_printing(use_latex = True)
from sympy import *

x,y,z,t= symbols("x y z t")
#insert f(x,y,...)

#funtion of any number of variables f(x,y,z)
origin = 


print('Given the function',latex((origin),mode='equation'),"the gradient is determined")

Dx = diff(origin,x)
Dy = diff(origin,y)

grad = (Dx, Dy)

print(grad)
display(grad)
