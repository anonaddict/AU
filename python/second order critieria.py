from sympy import init_printing
init_printing(use_latex = True)
from sympy import *

a,b,c,d,x,y,z,t= symbols("a b c d x y z t")

#insert f(x,y) and critical point here
origin = -x**2+12*x+2*y**2+24*y+32
crit = 6,-6
#input fields end here
#code is based on 3.2.2 "Anden ordens kriteriet" in "Calculus Beta 2021" by Niels Lauritzen, Klaus Thomsen, Steen Thorbjørn


a = diff(origin,x,x)
b = diff(origin,x,y)
c = diff(origin,x,y)
d = diff(origin,y,y)

asub = a.subs([(x,crit[0]),(y,crit[1])])
bsub = b.subs([(x,crit[0]),(y,crit[1])])
csub = c.subs([(x,crit[0]),(y,crit[1])])
dsub = d.subs([(x,crit[0]),(y,crit[1])])

print(a,b,c,d)

print(asub,bsub,csub,dsub)


det = asub*dsub-bsub*csub
print("the determinant of the hesse  matrix is")
print(det)

print("the critical point is therefore")

if det > 0 and asub > 0:
    print("local minimum")
elif det > 0 and asub < 0:
    print("local maximum")
elif det < 0:
    print("saddel")
else:
    print("no info")

