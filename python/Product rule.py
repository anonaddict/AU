#!/usr/bin/env python
# coding: utf-8

# In[3]:


#
#partiel integration reminder:
#\int f(x)g(x)\:dx=f(x)G(x)-\int f'(x)G(x)\:dx
#\int_a^b f(x)g(x)\:dx=[f(x)G(x)]_a^b-\int_a^b f'(x)G(x)\:dx


from sympy import init_printing
init_printing(use_latex = True)

from sympy import *

x,y,z,t,a,b,c,d= symbols("x y z t a b c d")

#insert the two functions inside the integral here a*b
a = x
b = exp(x*y)
var = y

prodrule = diff(a,var)*b+a*diff(b,var)

display(prodrule)


# In[ ]:




