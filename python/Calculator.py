from sympy import init_printing
init_printing(use_latex = True)
from sympy import *
#import numpy as np
#import matplotlib.pyplot as plt
import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))


from sympy.abc import x,y,z,a,b,c,d

og=y**2-x*y
c=x+1

test=og.subs(y,c)
xxx=test.expand()

print(xxx)

