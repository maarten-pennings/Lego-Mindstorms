@ECHO off
IF "(env) " neq "%PROMPT:~0,6%" ECHO Please run setup.bat first && EXIT /b

REM Run the pipeline
python prog1.py
python prog2.py
python prog3.py
python prog4.py
python prog5.py
