@echo off
chcp 65001 >nul
echo ==========================================
echo 多益網頁遊戲專案 - 自動部署工具
echo ==========================================
echo.

:: 檢查 Git 狀態
echo [1/3] 檢查本地 Git 狀態...
git status
echo.

:: 詢問提交說明
set "commit_msg="
set /p commit_msg="請輸入本次更新說明 (直接按 Enter 將使用自動時間戳): "

if "%commit_msg%"=="" (
    for /f "delims=" %%i in ('powershell -Command "Get-Date -Format 'yyyy-MM-dd HH:mm'"') do set datetime=%%i
    set "commit_msg=自動部署更新 (%%datetime%%)"
)

echo.
echo 準備提交，說明：%commit_msg%
echo.

:: 執行 Git 指令
echo [2/3] 正在新增並提交檔案...
git add .
git commit -m "%commit_msg%"
echo.

echo [3/3] 正在推送到 GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo.
    echo [錯誤] 推送失敗！請檢查您的網路或 GitHub 認證狀態。
    pause
    exit /b %errorlevel%
)

echo.
echo ==========================================
echo 部署指令已完成送出！
echo 網頁網址：https://TimLin7026.github.io/toeic-web-game/
echo (請等待 1 ~ 2 分鐘讓 GitHub Pages 更新完成)
echo ==========================================
echo.
pause
