# FPV-Drone-Control-Center

Одно и то же хранилище — два режима работы: «проводной» (wired) и «беспроводной» (wireless).
Выбирайте нужный режим и запускайте нужный скрипт.

# 📌 Возможности

Возможность	           Wired	  Wireless
ARM / DISARM	        ✅	        ✅
Управление каналами	    ✅	        ✅ (RC_OVERRIDE)
Телеметрия в браузере	✅	        ✅ (WebSocket)
Работает без Wi-Fi	    ✅	        ❌
Дальность	         1 м (USB)	   до 100 м (Wi-Fi 2.4/5 ГГц)
Задержка	         < 5 мс	       20-50 мс

📦 Быстрый старт
1. Клонирование
git clone https://github.com/Trytonottry/fpv-drone-control-center.git
cd FPV-Drone-Control-Center
cp .env.example .env          # отредактируйте при необходимости
chmod +x scripts/*.sh

2. Проводной режим (USB/UART)
Подходит для стендовых испытаний или когда RPi сидит на дроне и управляет напрямую.
Аппаратура

    FC Betaflight ↔ UART ↔ RPi
    Провод TX↔RX, RX↔TX, GND, 5 V

Запуск
./scripts/start_wired.sh

Откройте браузер: http://raspberrypi.local:5000

3. Беспроводной режим (Wi-Fi)
RPi Zero 2 W на дроне работает как компаньон, наземная станция — ноутбук/телефон.
Аппаратура

    FC Betaflight ↔ USB-TTL → RPi Zero 2 W
    RPi создаёт точку доступа или подключается к существующей сети
    Наземная станция в той же сети

Настройка RPi
sudo raspi-config
# Network Options → Hotspot (SSID=DroneControl, Pass=12345678)

Запуск
# На RPi Zero (onboard)
./scripts/start_onboard.sh

# На наземной станции
./scripts/start_ground.sh

Откройте браузер: http://localhost:5000 или http://192.168.4.1:5000
🔧 Настройка переменных окружения (.env)

Переменная	   Значение по-умолчанию	    Описание
MSP_DEVICE	   /dev/ttyS0	             UART для wired
BAUD_RATE	    115200	                 Скорость порта
DRONE_IP	  192.168.4.1	           IP дрона в wireless
ARM_CHANNEL	       0	                  Канал ARM
ANGLE_CHANNEL	   1	                Канал ANGLE/ACRO
ALTHOLD_CHANNEL	   2	                 Канал ALTHOLD

🐳 Docker
Сервис	  Назначение	               Команда
wired	  Проводной режим	        docker compose up wired
onboard	  Беспроводной (RPi)	    docker compose up onboard
ground	  Беспроводной (станция)	docker compose up ground

🔌 Порты/каналы Betaflight

    Ports → UART1 → MSP (115200)
    Configuration → Receiver → None (в wireless)
    Modes → ARM, ANGLE, ALTHOLD на нужных AUX-каналах.

🌐 API

Метод	URL	Параметры	        Описание
POST	/api/arm	            ARM моторов
POST	/api/disarm	—	        DISARM
GET	    /api/telemetry	        JSON телеметрия (wired)
WS	   ws://<drone_ip>:8765	    Поток телеметрии/RC (wireless)

🧪 Разработка без Docker

pip install -r src/requirements.txt
export PYTHONPATH=$PWD/src
# wired
python src/web/app.py
# wireless (ground)
DRONE_IP=192.168.4.1 python src/web/app.py

📄 Лицензия
MIT © 2024-2025 FPV-Drone-Control-Center.
