@ECHO off
IF "(env) " neq "%PROMPT:~0,6%" ECHO Please run setup.bat first && EXIT /b

REM Run the demos
python demo1.py
python demo2.py
python demo3.py
python demo4.py
python demo5.py
