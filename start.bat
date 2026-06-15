@echo off
title AI Career Guidance System
echo =======================================================
echo     Starting AI Career Guidance System
echo =======================================================
echo.
echo Launching the browser...
start http://127.0.0.1:8000/
echo Starting Django Server...
python manage.py runserver
pause
