@echo off
:: Устанавливаем кодировку UTF-8
chcp 65001 >nul
title Cloudflare WARP Monitor
cls

echo ======================================================
echo   Запуск мониторинга Cloudflare WARP...
echo   Окно должно быть открыто для работы скрипта.
echo ======================================================
echo.

:: Проверка Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ОШИБКА: Python не найден!
    pause
    exit /b
)

python warp_monitor.py
pause
