#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Sympy script til løsning af opgaver af typen
#Givet
#*Integral her.*
#find df(x)/dx ved hjælp af differentialreghningens fundamentalsætning


from sympy import init_printing
init_printing(use_latex = True)

from sympy import *

x,t,dt= symbols("x,t,dt")
#insert integral here
origin = t+6
#Lower and upper bounds 
limb = 1 
limt = x

fullint = Integral(origin, (t, limb, limt))

display(fullint)
print(latex(Integral(origin, (t, limb, limt))))

diffint = diff(fullint,x)

display(diffint)


# In[ ]:




