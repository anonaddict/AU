
from sympy import init_printing
init_printing(use_latex = True)

from sympy import *

x,y,z,t,a,b,c,d= symbols("x y z t a b c d")

#insert the function
f= 4*x*2*y+5*x*y**2+x**3
#point
pt = 2,1
#dir
vlen=10
directlen = 1/vlen
direct = 8,-6


fx = diff(f,x)
fy = diff(f,y)
print(fx,fy)


gradx = fx.subs([(x,pt[0]),(y,pt[1])])*directlen
grady = fy.subs([(x,pt[0]),(y,pt[1])])*directlen
print(gradx,grady)
gradlen=(sqrt(gradx**2+grady**2))
gx = gradx/gradlen
gy = grady/gradlen

print(gx,gy)

dufxy = gradx*direct[0]*directlen+grady*direct[1]*directlen



#print(dufxy)




# In[ ]:




