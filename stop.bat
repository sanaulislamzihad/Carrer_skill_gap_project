@echo off
title Stop AI Career Guidance System
echo =======================================================
echo     Stopping AI Career Guidance System (Port 8000)
echo =======================================================
echo.

FOR /F "tokens=5" %%T IN ('netstat -a -n -o ^| findstr "0.0.0.0:8000"') DO (
    SET /A ProcessId=%%T
    goto kill
)
FOR /F "tokens=5" %%T IN ('netstat -a -n -o ^| findstr "127.0.0.1:8000"') DO (
    SET /A ProcessId=%%T
    goto kill
)

echo No Django server found running on port 8000.
goto end

:kill
echo Found server process with PID: %ProcessId%. Terminating...
taskkill /F /PID %ProcessId%
echo.
echo Server stopped successfully.

:end
echo.
pause
