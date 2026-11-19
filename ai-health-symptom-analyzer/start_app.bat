 @echo off
title AI Health Symptom Analyzer
cd /d "%~dp0"

echo Starting AI Health Symptom Analyzer...

REM Open browser after 2 seconds in background
start "" cmd /c "timeout /t 2 /nobreak >nul && start http://127.0.0.1:5000"

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" app.py
) else if exist "..\.venv\Scripts\python.exe" (
    "..\.venv\Scripts\python.exe" app.py
) else (
    python app.py
)

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] App failed to start. Check if Python and Flask are installed.
    pause
)