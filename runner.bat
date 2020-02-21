@ECHO OFF

python --version 2>&1 | findstr "3."
if ERRORLEVEL 1 GOTO NOPY
pip --version> nul 2>&1
if ERRORLEVEL 1 GOTO NOPIP
ping -n 1 example.com> nul 2>&1
if ERRORLEVEL 1 GOTO NOIN
pip install --upgrade selenium
if exist Text_Repeat.py (
start "New Window" cmd /c python Text_Repeat.py
)
else (
START CMD /C "@echo off & mode con cols=40 lines=2 & ECHO %username% did something wrong && PAUSE"
)
exit

:NOIN
START CMD /C "@echo off & mode con cols=40 lines=2 & ECHO No Internet Connectivity && PAUSE"
GOTO :EOF

:NOPY
START CMD /C "@echo off & mode con cols=40 lines=2 & ECHO Python3 is not Found && PAUSE"
GOTO :EOF

:NOPIP
START CMD /C "@echo off & mode con cols=40 lines=2 & ECHO Pip3 is not Found && PAUSE"
