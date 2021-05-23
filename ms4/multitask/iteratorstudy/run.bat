@ECHO off
IF "(env) " neq "%PROMPT:~0,6%" ECHO Please run setup.bat first && EXIT /b

REM Run the demos
python study1.py
python study2.py
python study3.py
python study4.py
python study5.py
python study6.py
