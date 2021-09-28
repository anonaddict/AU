#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
SetTitleMatchMode, 2 ; searches for any instance of the specified string since many windows get named stuff like "Untitled - Notepad" which would require you to hardcode every document name.
SetNumLockState, AlwaysOn


#ifWinNotActive Jupyter

~^s::
reload
return

Numpad8::Send,
(
\begin{{}equation{}} \label{{}{}}

\end{{}equation{}}{Up}
)

Numpad9::Send,
(
\begin{{}math{}}

\end{{}math{}}{Up}
)

Numpad6::Send,
(
\int_{{}{}}{^}{{}{}}{Left 4}
)
Numpad4::Send,
(
\frac{{}{}}{{}{}}{Left}{Left}{Left}
)


Numpad5::Send,
(
\si[per-mode=symbol]{{}{}}{Left}
)


Numpad7::Send,
(
{{}{}}{Left}
)

Numpad2::Send,
(
\times10{^}{{}{}}{Left}
)



:r0*?:=>::
(
\Rightarrow
)


:r0*?:>=::
(
\geq
)


:r0*?:<=::
(
\leq
)


:r0*?:=/=::
(
\neq
)

:r0O*:10#::
(
\times10{^}{{}{}}{Left}
)

:*:align2#::
(
\begin{align*}
x&=y           &  w &=z              &  a&=b+c\\
2x&=-y         &  3w&=\frac{1}{2}z   &  a&=b\\
-4 + 5x&=2+y   &  w+2&=-1+w          &  ab&=cb
\end{align*}
)

:r0:lorentzgamma::
(
\gamma=\frac{{}1{}}{{}\sqrt{{}1-\frac{{}v{^}2{}}{{}c{^}2{}}{}}{}}{Enter}
)

:r0:lorentzbeta::
(
\beta=\sqrt{{}1-\frac{{}1{}}{{}\gamma{^}2{}}{}}
)

:r0:betavc::
(
\frac{{}v{}}{{}c{}}{}}
)

::tligevægt::
(
T_ligevægt=279\si{\kelvin}\sqrt{\frac{\sqrt{1-A}}{r}}
)

::vundvigelse::
(
v_{esc}=\sqrt{\frac{2GM}{r}}
)


:r0*:vm#::
(
Vm{(}f{)}=\left{(}0,\infty\right{]}
)


:r0*:dm#::
(
Dm{(}f{)}\forall x\in\R
)


:r0O:vec::
(
\vec{{}{}}{Left}
)

;::(::
;(
;\left(
;)

;::)::
;(
;\right)
;)

:r0O*:align#::
(
\begin{{}align{}} \label{{}{}}

\end{{}align{}}{Up}
)

:r0O*:eq#::
(
\begin{{}equation{}} \label{{}{}}

\end{{}equation{}}{Up}
)

:r0O:math#::
(
\begin{{}math{}}

\end{{}math{}}{Up}
)

:r0*?:kæderegl#::
(
(f\circ g)'=g'f'\circ g
)

:r0*?:freebody#::
(
\documentclass[tikz]{standalone}

\usetikzlibrary{arrows,calc}

\tikzset{
  >=stealth', % Change default arrow tip
  grid/.style={step=1cm,gray!30,very thin},
  axis/.style={thick,<->},
  vect/.style={ultra thick,->},
  vnode/.style={midway,font=\scriptsize},
  proj/.style={dashed,color=gray!50,->},
  poly/.style={fill=blue!30,opacity=0.3}
}

\begin{document}
\begin{tikzpicture}
  \coordinate (o)  at (0,0);   % origin
  \coordinate (g1) at (-5,-5); % grid bottom left
  \coordinate (g2) at (5,5);   % grid upper right
  % ---------------------------------------------
  \coordinate (V1) at (3,0.7);
  \coordinate (V2) at (-1.6,-3.7);
  \coordinate (Vr) at ($(V1) + (V2)$);

  % Parallelogram projection lines and polygon.
  \draw[proj] (V1) -- +(V2);
  \draw[proj] (V2) -- +(V1);
  \fill[poly] (o) -- (V1) -- (Vr) -- (V2) -- (o);

  % Grid rendering (bottom left) -- (upper right).
  \draw[grid] (g1) grid (g2);
  % Perpendicular X and Y axis.
  \draw[axis] (g1 |- o) -- (g2 |- o) node[anchor=east,xshift=15] {x};
  \draw[axis] (g1 -| o) -- (g2 -| o) node[anchor=north,yshift=15] {y};

  % Vector angles and lines
  \draw[color=blue,->] let \p{V} = (V1) in
    (0.75,0) arc (0:{atan(\y{V} / \x{V})}:0.75);
  \draw[color=blue,vect] (o) -- (V1) node [yshift=6, vnode] {$V_1$};

  \draw[color=blue,->] let \p{V} = (V2) in
    (0.5,0) arc (0:{atan(\y{V} / \x{V}) + 180}:0.5);
  \draw[color=blue,vect] (o) -- (V2) node [xshift=-7,vnode] {$V_2$};

  \draw[color=red,->] let \p{R} = (Vr) in
    (1,0) arc (0:{atan(\y{R} / \x{R}) + 360}:1);
  \draw[color=red, vect] (o) -- (Vr) node [xshift=8, vnode] {$V_R$};
\end{tikzpicture}
\end{document}
)

:r0*?:radtodeg::
(
1 rad =\frac{{}180\si{{}\degree{}}{}}{{}\pi{}}
)

:*:idiot#::
(
1=\cos{\alpha}^2+\sin{\alpha}^2
)


:*:intvedsub::
(
\int(f'\circ g)g'=f\circ g
)


:r0*?:degtorad::
(
1\si{{}\degree{}} =\frac{{}\pi{}}{{}180\si{{}\degree{}}{}}
)

:r0*?:c2k::
(
0\si[per-mode=symbol]{degreeCelcius} = 273.15\si[per-mode=symbol]{\kelvin}
)

:r0*?:k2c::
(
0\si[per-mode=symbol]{\kelvin}=-273.15\si[per-mode=symbol]{\degreeCelcius}
)


:r0*:dx::
(
\mathrm{{}d{}}x
)


:r0*:dy::
(
\mathrm{{}d{}}y
)


:r0*:dz::
(
\mathrm{{}d{}}z
)


:r0*:dt::
(
\mathrm{{}d{}}t
)


:*:code#::
(
\begin{verbatim}

\end{verbatim}
)

:r0:ul#::
(
\underline{{}\underline{{}{}}{}}{Left}{Left}
)

::constaccel::
(
Constant x-acceleration only:
v_x = v_{0x} + a{x}t
x = x_0 + v_{0x}t + \frac{1}{2}a_xt^2
v_x^2 = v_{0x}^2a_x(x-x_0)
x-x_0 = \frac{1}{2}(v_{0x} + v_x)t
)

:r0:emc2::
(
E=mc{^}2
)


:r0:csol::
(
299792458\si{{}m.s{^}{{}-1{}}{}}
)


:r0:gravity#::
(
F=G\frac{{}m_1m_2{}}{{}r{^}2{}}
)



:r0:pconst::
(
h=6.62607015\times10{^}{{}-34{}}\si{{}J.s{}}
)


:r0:gconst::
(
G=6.674\times10{^}{{}-11{}}\si{{}m{^}3.kg{^}{{}-1{}}.s{^}{{}-2{}}{}}
)

:r0:sbconst::
(
\sigma=5.670374419\times10{^}{{}-8{}}\si{{}W.m{^}{{}-2{}}.K{^}{{}-4{}}{}}
)

:r0:svt::
(
s=v_0t+\frac{{}1{}}{{}2{}}a \cdot t{^}2
)

:r0*:fig#::
(
\begin{{}figure{}}{[}htbp{]}
\centering
\includegraphics{[}scale=1{]}{{}filename.png{}}
\caption{{}caption{}}
\label{{}{}}
\end{{}figure{}}
)

::plot#::
(
\begin{tikzpicture}
\begin{axis}[
    axis lines = left,
    xlabel = $x$,
    ylabel = {$f(x)$},
]
%Below the red parabola is defined
\addplot [
    domain=-10:10, 
    samples=100, 
    color=red,
]
{x^2 - 2*x - 1};
\addlegendentry{$x^2 - 2x - 1$}
%Here the blue parabloa is defined
\addplot [
    domain=-10:10, 
    samples=100, 
    color=blue,
    ]
    {x^2 + 2*x + 1};
\addlegendentry{$x^2 + 2x + 1$}

\end{axis}
\end{tikzpicture}
)

::ga::
(
\vec{g}=
\begin{pmatrix}
0\\
-9.8
\end{pmatrix}\si{\meter\per\square\second}
)

::partint::
(
\int{f\cdot g'}=f\cdot g - \int{f'\cdot g}
)

::vec2::
(
\begin{pmatrix}
x\\
y
\end{pmatrix}
)

::vec3::
(
\begin{pmatrix}
x\\
y\\
z
\end{pmatrix}
)

::vec4::
(
\begin{pmatrix}
x\\
y\\
z\\
t
\end{pmatrix}
)

:r0:fma::
(
\vec{{}F{}}=m \cdot \vec{{}a{}}
)

::freefall#::
(
y=y_0+v{0y}t+\frac{1}{2}a_yt^2
)

::wfs::
(
W=\vec{F}s
)

:r0:angvel::
(
\omega=2\pi \cdot f
)

::xprod::
(
\overrightarrow{a}\times\overrightarrow{b}=\begin{pmatrix}\begin{vmatrix}a_2 & b_2\\a_3 & b_3\end{vmatrix}\\-\begin{vmatrix}a_1&b_1 \\a_3& b_3\end{vmatrix}\\\begin{vmatrix}a_1 & b_1\\a_2 & b_2\end{vmatrix}\end{pmatrix}=\begin{pmatrix}a_2b_3-a_3b_2\\a_3b_1-a_1b_3\\a_1b_2-a_2b_1\end{pmatrix}
)

::scalar#::
(
\overrightarrow{a}\times\overrightarrow{b}=\begin{pmatrix}\begin{vmatrix}a_2 & b_2\\a_3 & b_3\end{vmatrix}\\-\begin{vmatrix}a_1&b_1 \\a_3& b_3\end{vmatrix}\\\begin{vmatrix}a_1 & b_1\\a_2 & b_2\end{vmatrix}\end{pmatrix}=\begin{pmatrix}a_2b_3-a_3b_2\\a_3b_1-a_1b_3\\a_1b_2-a_2b_1\end{pmatrix}
)

:r0:reldopplerfull::
(
\omega'=\frac{{}1{}}{{}\sqrt{{}1-\frac{{}v{^}2{}}{{}c{^}2{}}{}}{}}\cdot \omega \cdot (1-\frac{{}v{}}{{}c{}}\cos{{}\phi{}})
)

:r0:reldoppler::
(
\omega'=\gamma\omega(1-\beta\cos{{}\phi{}})
)

:r0:limes::
(
\lim_{{}x\to0{}}
)

:r0:break#::
(
\vspace{{}2 mm{}}
)

::flux#::
(
\Phi_F=\frac{L_s}{2\pi r^2}
)

::lum#::
(
L=4\pi R^2 \sigma_{SB}T^4
)

::ijk::
(
\hat{i}\frac{\partial}{\partial x}+\hat{j}\frac{\partial}{\partial y}+\hat{k}\frac{\partial}{\partial z}
)

::jtoev::
(
1\si{J}==6.24\times10^{18} \electronvolt
)

::carttopolar::
(
\hat{r}=\cos{\phi}\hat{x}+\sin{\phi}\hat{y}, \hat{r}=-\sin{\phi}\hat{x}+\cos{\phi}\hat{y}
)


:R*O:header#::
(
\documentclass[12pt,a4paper]{article}
\title{Calculus $\beta$ or Mechanics and Thermodynamics}
\author{Rasmus Crolly}
\date{\today}

\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{pgfplots}

\usepackage{amsmath}
\usepackage{amssymb}

\usepackage[
backend=biber,
style=alphabetic,
sorting=ynt
]{biblatex}
\addbibresource{sources.bib}

\usepackage{siunitx}
\usepackage[cm]{fullpage}
\usepackage{listings}


\pgfplotsset{compat=1.16}
\usetikzlibrary{external}
\tikzexternalize[prefix=tikz/]

\newcommand{\R}{\mathbb{R}}

\setlength{\parindent}{0pt}

\usepackage{hyperref}
\hypersetup{
colorlinks=true,
linkcolor=blue,
filecolor=magenta,
urlcolor=cyan,
}				
\urlstyle{same}
	
	
\begin{document}
\maketitle

\begin{abstract}
Your abstract.
\end{abstract}
	
\section{Young and Freedman x.xx}
	
\subsection{1}

\begin{lstlisting}[language=Python]
\end{lstlisting}

\printbibliography[
heading=bibintoc,
title={References}
]
\end{document}
)



;O: Omit the ending character of auto-replace hotstrings when the replacement is produced. This is useful when you want a hotstring to be kept unambiguous by still requiring an ending character, but don't actually want the ending character to be shown on the screen. For example, if :o:ar::aristocrat is a hotstring, typing "ar" followed by the spacebar will produce "aristocrat" with no trailing space, which allows you to make the word plural or possessive without having to press Backspace. Use O0 (the letter O followed by a zero) to turn this option back off
;R: Send the replacement text raw; that is, without translating {Enter} to Enter, ^c to Control+C, etc. This option is put into effect automatically for hotstrings that have a continuation section. Use R0 to turn this option back off.
;* (asterisk): An ending character (e.g. Space, ., or Enter) is not required to trigger the hotstring.
;? (question mark): The hotstring will be triggered even when it is inside another word; that is, when the character typed immediately before it is alphanumeric. For example, if :?:al::airline is a hotstring, typing "practical " would produce "practicairline ". Use ?0 to turn this option back off.

;ClipSaved := ClipboardAll   ; Save the entire clipboard to a variable of your choice.
; ... here make temporary use of the clipboard, such as for pasting Unicode text via Transform Unicode ...
;Clipboard := ClipSaved   ; Restore the original clipboard. Note the use of Clipboard (not ClipboardAll).
;ClipSaved := ""   ; Free the memory in case the clipboard was very large.

