## Беспроводная связь

1. Подключите FC к RPi Zero 2 W через USB-TTL (3.3 V).  
2. Установите RPi Zero в режим точки доступа:  
sudo raspi-config → Network Options → Hotspot
SSID=DroneControl, Pass=12345678
или используйте существующую домашнюю сеть.  
3. На FC:  
Ports → UART1 → MSP (115200).  
Configuration → Receiver → None.  
4. Запустите `./scripts/start_onboard.sh` на RPi.  
5. На наземной станции: `./scripts/start_ground.sh`, затем http://localhost:5000
