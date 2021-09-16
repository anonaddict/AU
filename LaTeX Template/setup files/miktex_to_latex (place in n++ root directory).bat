:: Called from Notepad++ Run  
:: [path_to_bat_file] "$(CURRENT_DIRECTORY)" "$(NAME_PART)"  

:: Change Drive and  to File Directory  
%~d1  
cd %1

:: Run Cleanup  
call:cleanup  

:: Run pdflatex -&gt; bibtex -&gt; pdflatex -&gt; pdflatex  
pdflatex %2  
bibtex  %2  
:: If you are using multibib the following will run bibtex on all aux files  
:: FOR /R . %%G IN (*.aux) DO bibtex %%G  
pdflatex %2  
pdflatex %2  

:: Run Cleanup  
call:cleanup  

:: Open PDF  
START "" "C:\Users\admin\AppData\Local\SumatraPDF\SumatraPDF.exe" %3 -reuse-instance  

:: Cleanup Function  
:cleanup  
del *.dvi
del *.out
del *.log 
del *.aux  
del *.bbl    
del *.blg  
del *.brf  
del *.xml
del *.bcf
goto:eof  