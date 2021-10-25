#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import init_printing
init_printing(use_latex = True)
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

from sympy.abc import x,y,z,a,b,c,d

fxy = 2*x*y+y**2
pink = 3

fxyn= fxy.subs(x,pink)

print("fx =",fxyn)


# In[ ]:




