@echo off
echo Starting CyberWise application...

:: 确保在正确的目录中运行
cd /d "%~dp0"

:: 运行模型设置脚本
echo Running setup script...
call setup_models.bat
if errorlevel 1 (
    echo Setup failed! Please check the error messages above.
    pause
    exit /b 1
)

:: 启动 Python API 服务器
echo Starting Python API server...
start cmd /k "cd api && python text_analyzer.py"

:: 启动 Web 服务器
echo Starting Web server...
start cmd /k "python -m http.server 8000"

echo.
echo API server running at: http://localhost:5000
echo Web server running at: http://localhost:8000
echo.
echo Access the application at: http://localhost:8000/templates/login.html
echo.
echo Press Ctrl+C in each window to stop the servers
pause 