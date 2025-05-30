import serial  # import serial pacakge
import mysql.connector
from datetime import datetime
import time
arduino = serial.Serial('COM5', 9600, timeout=.1)
time.sleep(2)
arduino.write(b'1')
time.sleep(0.5)