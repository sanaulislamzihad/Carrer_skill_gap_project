@echo off
title AI Career Guidance System
echo =======================================================
echo     Starting AI Career Guidance System
echo =======================================================
echo.

:: Check for Python
echo Checking if Python is installed...
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not added to your PATH!
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check the box "Add Python to PATH" during installation.
    pause
    exit /b
)
echo [OK] Python is installed.
echo.

:: Check for pip
echo Checking if PIP is installed...
pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [WARNING] PIP is not found! Attempting to fix...
    python -m ensurepip
)
echo [OK] PIP is installed.
echo.

:: Install dependencies from requirements.txt quietly
echo Checking and installing required packages (this may take a moment)...
pip install -r requirements.txt --quiet
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to install required packages!
    pause
    exit /b
)
echo [OK] All requirements are satisfied!
echo.

:: Start the Application
echo Launching the browser...
start http://127.0.0.1:8000/

echo Starting Django Server...
python manage.py runserver

pause
