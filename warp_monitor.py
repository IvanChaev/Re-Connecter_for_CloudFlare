import subprocess
import time
import os

# Конфигурация
TARGET_HOST = "8.8.8.8"  # Адрес для проверки связи
CHECK_INTERVAL = 10      # Проверка каждые 10 секунд
MAX_LATENCY = 500        # Если пинг выше 500мс — переподключаем (опционально)

def check_connection():
    """Проверяет доступность сети через ping."""
    # Параметр -n для Windows, -c для Linux/macOS
    param = '-n' if os.name == 'nt' else '-c'
    command = ['ping', param, '1', TARGET_HOST]
    
    return subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0

def reconnect_warp():
    """Выполняет цикл переподключения."""
    print(f"[{time.strftime('%H:%M:%S')}] Потеря связи или лаги. Переподключаю WARP...")
    try:
        subprocess.run(["warp-cli", "disconnect"], check=True)
        time.sleep(2)
        subprocess.run(["warp-cli", "connect"], check=True)
        print("Переподключение выполнено.")
    except Exception as e:
        print(f"Ошибка при попытке переподключения: {e}")

def monitor():
    print(f"Мониторинг Cloudflare WARP запущен (цель: {TARGET_HOST})...")
    while True:
        if not check_connection():
            reconnect_warp()
            # Даем время на установку соединения после реконнекта
            time.sleep(10)
        else:
            # Связь в порядке
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor()
