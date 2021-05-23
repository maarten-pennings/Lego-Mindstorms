@ECHO OFF

SET LOC=C:\Users\maarten\AppData\Local\Programs\Python\Python39

REM Safety check: is there a Python 3.8
FOR /F "tokens=1,2,3 delims=. " %%I IN ('%LOC%\python --version 2^> nul') DO IF "%%I" EQU "Python" IF "%%J" EQU "3" IF "%%K" GEQ "8" goto :PythonAvail
ECHO ERROR: No Python 3.8 or higher available
EXIT /b

:PythonAvail
ECHO Found correct version of Python; creating virtual env
%LOC%\python.exe -m venv env
CALL env\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel
IF EXIST requirements.txt (
   pip install -r requirements.txt
)
ECHO 'setup' done, now 'run'
