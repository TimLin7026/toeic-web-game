@echo off
echo ==========================================
echo TOEIC Web Game - Auto Deploy Tool
echo ==========================================
echo.

:: [1/3] Checking git status
echo [1/3] Checking local Git status...
git status
echo.

:: Get commit message
set "commit_msg="
set /p commit_msg="Enter commit message (Press Enter for auto timestamp): "

if "%commit_msg%"=="" (
    for /f "delims=" %%i in ('powershell -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"') do set datetime=%%i
    set "commit_msg=Auto deploy (%%datetime%%)"
)

echo.
echo Committing with message: %commit_msg%
echo.

:: [2/3] Add and commit
echo [2/3] Adding and committing files...
git add .
git commit -m "%commit_msg%"
echo.

:: [3/3] Push to GitHub
echo [3/3] Pushing to GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Push failed! Please check your network or GitHub credentials.
    pause
    exit /b %errorlevel%
)

echo.
echo ==========================================
echo Deployment completed!
echo URL: https://TimLin7026.github.io/toeic-web-game/
echo (Please wait 1-2 minutes for GitHub Pages to update)
echo ==========================================
echo.
pause
