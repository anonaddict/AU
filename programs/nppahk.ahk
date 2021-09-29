#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetTitleMatchMode, 2 ; searches for any instance of the specified string since many windows get named stuff like "Untitled - Notepad" which would require you to hardcode every document name.


#ifWinActive Notepad

~^s::
reload
return

:r0O*:qq::
(
{{}{{}{}}{{}{}}{}}{Left 3}
)


:r0O*:zz::
(
{{}{}}{Left}
)
