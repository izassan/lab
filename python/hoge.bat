@echo off
set TOOLD_HOME="C:\Users\Izassan\local\projects\izassan.net\izassan\lab\python\packages"
set PYTHONPATH="%TOOLD_HOME%:%PYTHONPATH%"

python "%TOOLD_HOME%\..\main.py" %*
