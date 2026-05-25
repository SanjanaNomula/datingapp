@echo off
echo Starting SRM Match Local Server...
cd /d "%~dp0"

REM Check for common virtual environment names and activate if found
IF EXIST "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) ELSE IF EXIST "env\Scripts\activate.bat" (
    call env\Scripts\activate.bat
) ELSE (
    echo [Warning] No virtual environment 'venv' or 'env' found. Using global Python.
)

python manage.py runserver
pause