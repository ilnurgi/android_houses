# coding: utf-8

"""
читаем данные сериного порта и выводим данные 
"""

import sys
import serial

arduino_tty = '/dev/ttyACM0'
speed = 9600

ser = serial.Serial(arduino_tty, speed)
print 'connect to {0}, speed={1}\nwhite data\n'
while True:
    print ser.readline()
