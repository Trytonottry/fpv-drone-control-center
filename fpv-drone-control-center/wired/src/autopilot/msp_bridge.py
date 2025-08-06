import serial, struct, time
import pymsp
from .config import MSP_DEVICE, BAUD_RATE

class MSPBridge:
    def __init__(self):
        self.ser = serial.Serial(MSP_DEVICE, BAUD_RATE, timeout=1)
        self.board = pymsp.Board(self.ser)

    def arm(self):
        self.board.set_channel(ARM_CHANNEL, 1800)
        self.board.send_rc()

    def disarm(self):
        self.board.set_channel(ARM_CHANNEL, 1000)
        self.board.send_rc()

    def set_mode(self, channel, value_us):
        self.board.set_channel(channel, value_us)
        self.board.send_rc()

    def get_attitude(self):
        return self.board.get_attitude()