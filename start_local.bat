@echo off
echo Starting CyberWise local server...
echo.
echo Access the application at: http://localhost:8000/templates/login.html
echo.
echo Press Ctrl+C to stop the server
echo.

python -m http.server 8000 