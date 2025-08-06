import os
MSP_DEVICE = os.getenv("MSP_DEVICE", "/dev/ttyS0")
BAUD_RATE  = int(os.getenv("BAUD_RATE", 115200))
ARM_CHANNEL   = int(os.getenv("ARM_CHANNEL", 0))
ANGLE_CHANNEL = int(os.getenv("ANGLE_CHANNEL", 1))
ALTHOLD_CHANNEL = int(os.getenv("ALTHOLD_CHANNEL", 2))