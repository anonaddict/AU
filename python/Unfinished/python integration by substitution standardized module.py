#Script to standardize integration by substitution


from sympy import init_printing
init_printing(use_latex = True)

from sympy import *

x,y,z,u, du, dx,b_o,b_n= symbols("x y z u du dx b_{old} b_{new}")


#insert integral and u here
origin = -log(2*x)/x
v = x**5
#Lower and upper bounds 
limb = 0 
limt = 0.5



print('given the integral')

originint = Integral(origin, (x, limb, limt))

print(latex((Integral(origin, (x, limb, limt))),mode='equation'))

print('integration by substitution is performed by selecting')
print('u =',v)

print('$u$ is then differentiated and the expression for $\\mathrm{d}x$ is isolated')
dv = diff(v,x)

dudx = Eq(du*dx**-1, dv)


print('\\begin{equation}\\frac{\\mathrm{d}u)}{\\mathrm{d}x}=',latex(dv),'\end{equation}')

dudv = dv**-1

print('\\begin{equation}\\mathrm{d}x=',solve(dudx,dx),'\\end{equation}')

dxtodu = origin*dudv

print('the new $u$-boundaries are calculated by inserting the old $x$-boundaries in the expression for $u$')

templim = ([v.subs(x,b_o)])

print('\\begin{equation} b_{new} =',templim,'\\end{equation}')

newlimb = ([v.subs(x,limb)])
newlimt = ([v.subs(x,limt)])

print('In this case the new bounds for the lower and upper bounds respectively are',newlimb,'and',newlimt)
print('when the new boundaries are inserted the new $u$-integral is')

newint = Integral(dxtodu,(u,newlimb,newlimt))
newintsub = newint.subs(v,u)

print(latex((newintsub),mode='equation'))

#solvint = integrate(newint)
