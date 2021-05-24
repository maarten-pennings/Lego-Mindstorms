@ECHO OFF

REM If Python is not in your PATH set the PYTHONDIR manually (must end in \)
REM SET PYTHONDIR=C:\Users\maarten\AppData\Local\Programs\Python\Python39\

REM Safety check: is there a Python 3.8
FOR /F "tokens=1,2,3 delims=. " %%I IN ('%PYTHONDIR%python --version 2^> nul') DO IF "%%I" EQU "Python" IF "%%J" EQU "3" IF "%%K" GEQ "8" goto :PythonAvail
ECHO ERROR: No Python 3.8 or higher found
EXIT /b

:PythonAvail
ECHO Found correct version of Python; creating virtual env
%PYTHONDIR%python.exe -m venv env
CALL env\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel
IF EXIST requirements.txt (
   pip install -r requirements.txt
)
ECHO 'setup' done, now 'run'
