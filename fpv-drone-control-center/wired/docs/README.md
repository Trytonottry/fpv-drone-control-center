# FPV Drone Control Center

Простая и расширяемая система управления FPV-дронами на базе Betaflight и Raspberry Pi.

## Возможности
- ARM / DISARM через веб-интерфейс  
- Получение телеметрии (Attitude, RC channels)  
- RESTful API и WebSocket для UI  
- Контейнеризация Docker для быстрого разворачивания  

## Требования
- Raspberry Pi 3/4 с Raspberry Pi OS 64-bit  
- Flight Controller с Betaflight ≥ 4.4 и включённым MSP OVERRIDE  
- Кабель UART между FC и RPi (`/dev/ttyS0` или `/dev/serial0`)

## Установка
1. Клонируйте репозиторий  
git clone https://github.com/yourname/FPV-Drone-Control-Center.git
cd FPV-Drone-Control-Center
2. Скопируйте `.env.example` в `.env` и отредактируйте переменные, если нужны другие UART/каналы.  
3. Запустите  
chmod +x scripts/*.sh
./scripts/start.sh
4. Откройте браузер: http://raspberrypi.local:5000

## Разработка
- Все исходники в `src/`.  
- Для запуска без Docker:  
pip install -r src/requirements.txt
export PYTHONPATH=$PWD/src
python src/web/app.py

## API
- `POST /api/arm`   – ARM моторов  
- `POST /api/disarm`– DISARM  
- `GET  /api/telemetry` – JSON с текущей телеметрией (WebSocket в будущем)

## Лицензия
MIT
