#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetTitleMatchMode, 2 ; searches for any instance of the specified string since many windows get named stuff like "Untitled - Notepad" which would require you to hardcode every document name.
#IfWinActive Jupyter Notebook

~^s::
reload
return

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
)

:r0*?:^::**

