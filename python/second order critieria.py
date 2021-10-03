from sympy import init_printing
init_printing(use_latex = True)
from sympy import *

a,b,c,d,x,y,z,t= symbols("a b c d x y z t")

#insert f(x,y) and critical point here
origin = -x**2+12*x+2*y**2+24*y+32
crit = 6,-6

a = diff(origin,x,x)
b = diff(origin,x,y)
c = diff(origin,x,y)
d = diff(origin,y,y)

ain = a.subs([(x,crit[0]),(y,crit[1])])
bins = b.subs([(x,crit[0]),(y,crit[1])])
cin = c.subs([(x,crit[0]),(y,crit[1])])
din = d.subs([(x,crit[0]),(y,crit[1])])

print(a,b,c,d)

print(ain,bins,cin,din)


det = ain*din-bins*cin
print("the determinant of the hesse  matrix is")
print(det)

print("the critical point is therefore")

if det > 0 and ain > 0:
    print("local minimum")
elif det > 0 and ain < 0:
    print("local maximum")
elif det < 0:
    print("saddel")
else:
    print("no info")

