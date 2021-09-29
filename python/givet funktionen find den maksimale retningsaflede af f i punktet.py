#!/usr/bin/env python
# coding: utf-8

# In[21]:



#script til løsning af sci2u opgaver af typen
#givet funktionen
#find den maksimale retningsafledede af f i punktet


#jf sætning 3.16
#Lad f : \mathcal{D}(f) \to \mathbb Rf:D(f)→R være en funktion hvis partielt afledede eksisterer og er kontinuerte. 
#Da gælder, at den maksimale værdi af den retningsafledte D_{\bar{u}}f(x,y)
#er længden ∥∇f(x,y)∥ af gradienten, og denne antages, når enhedsvektoren \bar{u}
#har samme retning som gradienten ∇f(x,y)



from sympy import init_printing
init_printing(use_latex = True)
from sympy import *

x,y,z,t= symbols("x y z t")

#funtion 
origin = 4*x*y
#variable values for defined point
xval = 2
yval = -1



Dx = diff(origin,x)
Dy = diff(origin,y)

grad = (Dx, Dy)
print(grad)

gradx = grad[0].subs([(x,xval),(y,yval)])
grady = grad[1].subs([(x,xval),(y,yval)])
vlen = sqrt(gradx**2+grady**2)


print("result =",vlen)



# In[9]:





# In[ ]:




