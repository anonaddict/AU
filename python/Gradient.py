
from sympy import init_printing
init_printing(use_latex = True)
from sympy import *

x,y,z,t= symbols("x y z t")
#insert f(x,y,...)

#funtion of any number of variables f(x,y,z)
origin = 2*x**3+y**2-24*x-6*y+5
originsubs=origin.subs(y,2/5)
Dx = diff(originsubs,x)
Dy = diff(originsubs,y)

grad = (Dx, Dy)


print(grad)



