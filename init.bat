@echo off
call pipenv run python init.py
start /b del init.bat
@echo on