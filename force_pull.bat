@echo off
echo ==========================================
echo WARNING: Force Overwrite Local with GitHub
echo ==========================================
echo.
echo This will DISCARD all your local changes!
echo.
set /p confirm="Are you sure you want to proceed? (y/n): "

if /i "%confirm%"=="y" (
    echo.
    echo [1/2] Fetching from GitHub...
    git fetch origin
    echo.
    echo [2/2] Force resetting to origin/main...
    git reset --hard origin/main
    echo.
    echo Done! Your local files now match GitHub exactly.
) else (
    echo.
    echo Canceled.
)
echo.
pause
