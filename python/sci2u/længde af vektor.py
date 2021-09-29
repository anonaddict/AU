#!/usr/bin/env python
# coding: utf-8

# In[13]:


from sympy import init_printing
init_printing(use_latex = True)
from sympy import *

vec = 2,1
vlen = sqrt(vec[0]**2+vec[1]**2)
print("2d length =",vlen)

#vlen3d = sqrt(vec[0]**2+vec[1]**2+vec[2]**2)


# In[ ]:




