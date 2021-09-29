
#script til løsning af sci2u opgaver af typen
#find gradienten af funktionen
#function
#i punktet
#point

from sympy import init_printing
init_printing(use_latex = True)
from sympy import *

x,y,z,t= symbols("x y z t")
#insert f(x,y,...)

#funtion of any number of variables f(x,y,z)
origin = 1/(x**4*y**2)
#variable values for defined point
xval = -2
yval = -1

print('Given the function',latex((origin),mode='equation'),"the gradient is determined")

Dx = diff(origin,x)
Dy = diff(origin,y)

grad = (Dx, Dy)


print(grad)


defdx = Dx.subs([(x,xval),(y,yval)])
defdy = Dy.subs([(x,xval),(y,yval)])


print("the gradient in the given point is")
defgrad = (defdx, defdy)

print(defgrad)




