Для использования вам нужно установить для начала Python версии 3.11 и выше.
Запустите run_warp_monitor.bat и наслаждайтесь авто-переподключение в cloud flare в случае
плохого интернета.

# Re-Connecter for Cloudflare WARP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Автоматический мониторинг и переподключение Cloudflare WARP при обрыве связи.  
Полезен для стран с нестабильным интернетом или частыми блокировками.

## 🚀 Возможности

- Проверяет доступность интернета пингом до `8.8.8.8`.
- При потере соединения автоматически выполняет `warp-cli disconnect` → `connect`.
- Работает в фоновом режиме (можно запустить как демон).
- Кроссплатформенный (Windows, Linux, macOS).

## 📦 Требования

- Установленный [Cloudflare WARP](https://one.one.one.one/).
- Python 3.6+ (стандартная библиотека, дополнительные пакеты не нужны).

## 🔧 Установка и запуск

1. Склонируйте репозиторий или скачайте `warp_monitor.py`:
   ```bash
   git clone https://github.com/yourusername/Re-Connecter_for_CloudFlare.git
   cd Re-Connecter_for_CloudFlare
