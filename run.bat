@echo off
REM Quick launcher for Artist Sculpture Cost Prediction
echo ===================================================
echo   Artist Sculpture Cost Prediction System
echo ===================================================
echo.
echo Starting development server...
echo Access the application at: http://127.0.0.1:8000
echo Press Ctrl+C in this terminal window to stop the server.
echo.
python manage.py runserver 127.0.0.1:8000
pause
