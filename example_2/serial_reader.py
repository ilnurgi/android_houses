# coding: utf-8

"""
читаем данные сериного порта и выводим данные 
"""

import sys
import time

import serial

arduino_tty = '/dev/ttyACM0'
speed = 9600

try:
    ser = serial.Serial(arduino_tty, speed)
except serial.serialutil.SerialException as err:
    print 'device {0}, not found'.format(arduino_tty)
    print unicode(err)
    exit(0)
else:
    print 'connect to {0}, speed={1}\nwhite data\n'.format(arduino_tty, speed)


while True:
    try:
        print ser.readline()
        counter = 1
    except serial.serialutil.SerialException:
        print '{0}/10 error get data'.format(counter)
        time.sleep(5)
        counter += 1
        if counter > 10:
            break