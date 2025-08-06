import threading, time
from .msp_bridge import MSPBridge

class Autopilot(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.bridge = MSPBridge()
        self.running = True

    def run(self):
        while self.running:
            att = self.bridge.get_attitude()
            # Пример стабилизации: держим уровень
            print(att)
            time.sleep(0.1)

    def stop(self):
        self.running = False