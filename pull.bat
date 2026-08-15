@echo off
echo ==========================================
echo TOEIC Web Game - Auto Pull Tool
echo ==========================================
echo.
echo [1/2] Fetching changes from GitHub...
git fetch origin
echo.
echo [2/2] Pulling latest code...
git pull origin main
echo.
echo ==========================================
echo Local files are now up to date with GitHub!
echo ==========================================
echo.
pause
