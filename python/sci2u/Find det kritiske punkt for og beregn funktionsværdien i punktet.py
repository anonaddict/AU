#!/usr/bin/env python
# coding: utf-8

# In[65]:



#script til løsning af sci2u opgaver af typen
#find det kritiske punkt for
#function
#og beregn funktionsværdien i punktet

from sympy import init_printing
init_printing(use_latex = True)
from sympy import *

x,y,z,t= symbols("x y z t")

#funtion of any number of variables f(x,y,z)
origin = x**2-4*x+y**2-6*y+13


print('Given the function',latex((origin),mode='equation'),"the gradient is determined")


Dx = diff(origin,x)
Dy = diff(origin,y)

grad = (Dx, Dy)
print(Dx,Dy)
defeqx = Eq(Dx,0)
defeqy = Eq(Dy,0)
solveq = solve((defeqx,defeqy),x,y)

print("the critical point is")
print(solveq)

print("the function value in the critical point is")


funcval = origin.subs([(x,solveq[x]),(y,solveq[y])])

print(funcval)


#print(grad)
#display(grad)



#defdx = Dx.subs([(x,xval),(y,yval)])
#defdy = Dy.subs([(x,xval),(y,yval)])


#print("the gradient in the given point is")
#defgrad = (defdx, defdy)
#display(defgrad)


# In[ ]:





# In[ ]:




