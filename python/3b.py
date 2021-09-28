#!/usr/bin/env python
# coding: utf-8

# In[44]:



from sympy import init_printing
init_printing(use_latex = True)
from sympy import *

x,y,z,t,f,fm,g,gm,v= symbols("x y z t f fm g gm v")
#insert f(x,y,...)
origin = x**2*sin(pi*y**2)

constx = x**2
compfunc2 = (sin(pi*y**2))


var1 = x
var2 = y

a2 = sin(y)
b2 = pi*y**2

c2 = diff(a2,var2)
d2 = diff(b2,var2)

#upper bounds if integral 
#limb = 1 
#limt = x
#insert the functions inside here

#fullint = Integral(origin, (t, limb, limt))
#display(fullint)


print('Given the function',latex((origin),mode='equation'),'the partial derivative for a given variable is determined by differentiating the original function with the respective variable and keeping all other variables constant ' )

partx = diff(origin,x)
party = diff(origin,y)

print("$f_x$ is therefore")

print('\\begin{equation} f_x = \\frac{\partial}{\partial x} =',latex(partx),'\\end{equation}')

print("Differentiating $f(x,y)$ for $y$ requires differentiating the function $",latex(compfunc2),".$")

print('Since this is a composite function the chain rule is used')
chainrule = "(f(g(x)))'=f'(g(x))\cdot g'(x)"
print("\\begin{equation}",chainrule,"\\end{equation}")


#int f(x)g(x)\:dx=f(x)G(x)-\int f'(x)G(x)\:dx
#\int_a^b f(x)g(x)\:dx=[f(x)G(x)]_a^b-\int_a^b f'(x)G(x)\:dx

print("the following functions are chosen as f and g respectively")

f2 = a2
g2 = b2


fm2 = c2
gm2 = d2
chain = fm2.subs(var2,g2)*gm2
cconst = constx*fm2.subs(var2,g2)*gm2


print("\\begin{equation} f =",latex(f2),",\;","g =",latex(g2),"\\end{equation}")
print("this means f' and g' become")

print("\\begin{equation} f' =",latex(fm2),",\;","g' =",latex(gm2),"\\end{equation}")

print("these can now all be inserted into the chain rule")

print("\\begin{equation}",latex(chain),'\\end{equation}')

print("then multiply with the constant $",latex(constx),"$ to obtain the full expression for $f_y$")


print("\\begin{equation} f_y = \\frac{\partial}{\partial y} =",latex(cconst),'\\end{equation}')

print("Finally inputting the original equation in a CAS program and finding the partially derived for y returns")

print('\\begin{equation} f_y = \\frac{\partial}{\partial y} =',latex(party),'\\end{equation}')

print("which suggests the method used was correct")

