#!/usr/bin/env python
# coding: utf-8

# In[29]:



from sympy import init_printing
init_printing(use_latex = True)

from sympy import *

x,y,z,t,a,b,c,d= symbols("x y z t a b c d")

#insert the function
f= x*y
#point
pt = -1,-2
#dir
u=2
directlen = 1/sqrt(u)
direct = -1,1


fx = diff(f,x)
fy = diff(f,y)
print(fx,fy)



gradx = fx.subs([(x,pt[0]),(y,pt[1])])
grady = fy.subs([(x,pt[0]),(y,pt[1])])
print(gradx,grady)

#gradlen = sqrt(gradx**2+grady**2)

scalar = (gradx*direct[0]+grady*direct[1])*directlen

print(scalar)




# In[ ]:




