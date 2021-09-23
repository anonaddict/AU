#!/usr/bin/env python
# coding: utf-8

# In[12]:


from sympy.plotting import plot 
from sympy import * 


x = Symbol('x')
G=6.674*10**(-11)
M=5.972*10**(24)
m=1
r=6.37*10**6

F = ((G*(M*m))/((r-x)**2))
epot=m*F*(-x)
plot(epot,(x,-100000,-10000),axis_center=(0,0),xlim=(-120000,0),ylim=(0,1000000))




# In[10]:


from sympy import *   
x,v = symbols('x v')
  # man kan også istedet skrive f = x**(1/2)   
G=6.674*10**(-11)
M=5.972*10**(24)
m=1
r=6.37*10**6

F1 = ((G*(M*m))/((r+100000)**2))
F2 = ((G*(M*m))/((r+10000)**2))
epot1=m*F1*100000
epot2=m*F2*10000
print(epot1)
print(epot2)
etot=epot1-epot2

print(etot,'J')

v10=solve(Eq(etot,1/2*m*v**2),v)

solkmh=sol[1]*3.6

print(v10[1].evalf(5),'m/s')
print(solkmh.evalf(5),'km/h')



# In[28]:


from sympy import *
from sympy.plotting import plot 
a,m,g,v=symbols('a m g v')

D = 1.3*10**(-3)
F_t= m*g
F_gnid= D*v**2

ans2 = solve(Eq(m*a,F_gnid-F_t),a)

print(ans2[0])
#så A=0.0013 og C=9.82=g
plot(ans2[0],(v,0,1500))


# In[142]:





# In[ ]:




