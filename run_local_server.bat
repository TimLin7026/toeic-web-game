@echo off
title TOEIC Web Game - Local Server
echo ==========================================================
echo   TOEIC Web Game Local Server is starting...
echo   Local URL: http://localhost:8000
echo.
echo   Please DO NOT close this command prompt window.
echo   Close this window to stop the server after testing.
echo ==========================================================
echo.

:: Open in default browser
start http://localhost:8000

:: Start Python HTTP Server
python -m http.server 8000
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Server failed to start! Port 8000 might be in use.
    echo.
    pause
)
