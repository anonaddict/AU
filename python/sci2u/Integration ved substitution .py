#!/usr/bin/env python
# coding: utf-8

# In[118]:


#Sympy script til løsning af opgaver af typen
#Hvordan ser integralet
#*Integral her.*
#Ud efter substitutionen
#*u eller t substitution her.*

from sympy import init_printing
init_printing(use_latex = True)

from sympy import *

x, u, du, dx= symbols("x u du dx")
#insert integral and u here
origin = -log(2*x)/x
v = 2*x
#Lower and upper bounds 
limb = 0 
limt = 0.5

originint = Integral(origin, (x, limb, limt))

display(originint)
print(latex(Integral(origin, (x, limb, limt))))

dv = diff(v,x)

print('u =',v)

dudx = Eq(du*dx**-1, dv)

display(dudx)

dudv = dv**-1
print(dudv)

dxtodu = origin*dudv

newlimb = ([v.subs(x,limb)])
newlimt = ([v.subs(x,limt)])
print('new bottom limit is now',newlimb,'and the new top',newlimt)

newint = Integral(dxtodu,(u,newlimb,newlimt))
newintsub = newint.subs(v,u)

print('final solution is therefore:')
display(newintsub)
print(latex(newintsub))

