#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Sympy script til løsning af opgaver af typen
#Løses
#*Integral her.*
#med partiel integration fås
#*udtryk*
#hvad skal der stå i boksen?
#
#partiel integration reminder:
#\int f(x)g(x)\:dx=f(x)G(x)-\int f'(x)G(x)\:dx
#\int_a^b f(x)g(x)\:dx=[f(x)G(x)]_a^b-\int_a^b f'(x)G(x)\:dx


from sympy import init_printing
init_printing(use_latex = True)

from sympy import *

x,y,z,t,a,b,c,d= symbols("x y z t a b c d")

#insert the two functions inside the integral here
a = x
b = -cos(x)

c = integrate(b,x)
d = diff(a,x)

#fullint = a*c-Integral(d*c,x)
#display(fullint)
#print(latex(fullint))

print('c:')
display(c)
print('d:')
display(d)


# In[ ]:





# In[ ]:




