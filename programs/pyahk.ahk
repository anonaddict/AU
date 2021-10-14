#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetTitleMatchMode, 2 ; searches for any instance of the specified string since many windows get named stuff like "Untitled - Notepad" which would require you to hardcode every document name.


~^s::
reload
return

#IfWinActive Jupyter Notebook

:r0*?O:print::
(
print{(}{"}{"}{)}{Left 2}
)

:r0*?:pytex::
(
print{(}{"}{\}{\}{[}{"}{,}latex(){,}{"}{.}{\}{\}{]}{"}{)}{Left 9}
)

:r0*?:imports::
(
from sympy import init_printing
init_printing(use_latex = True)
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

from sympy.abc import x,y,z,a,b,c,d

)

:r0*?:^::**

:r0*?:withplot::
(
# library
import numpy as np
import matplotlib.pyplot as plt

# Create data
x=range(1,6)
y=[1,4,6,8,4]

# Area plot
plt.fill_between(x, y)
plot.show()
)

:r0*?:npmat::
(
import numpy as np

A = np.arange(4)
print('A =', A)

B = np.arange(12).reshape(2, 6)
print('B =', B)

)