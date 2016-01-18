# coding: utf-8

"""
читаем данные сериного порта и выводим данные 
"""

import sys
import time

import requests
import serial

arduino_tty = '/dev/ttyACM0'
speed = 9600

try:
    ser = serial.Serial(arduino_tty, speed)
except serial.serialutil.SerialException:
    print 'device {0}, not found'.format(arduino_tty)
    exit(0)
else:
    print 'connect to {0}, speed={1}\nwhite data\n'.format(arduino_tty, speed)


while True:
    try:
        data = ser.readline()
        data = int(data.replace('\r', '').replace('\n', ''))
        requests.post('http://ilnurgi1.ru/arduino/', data={'light': data})
        counter = 1
    except serial.serialutil.SerialException:
        print '{0}/10 error get data'.format(counter)
        time.sleep(5)
        counter += 1
        if counter > 10:
            break