# coding: utf-8

"""
читаем данные сериного порта
и при изменении данных, отправляемых их на сервер
"""

import datetime
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

corridor_light_last = -1
counter = 1
counter_max = 10

while True:
    try:
        data = ser.readline()        
    except serial.serialutil.SerialException:
        print '{0}/{1} error get data'.format(counter, counter_max)
        time.sleep(5)
        if counter > counter_max:
            break
        counter += 1
    else:
        corridor_light = int(data.replace('\r', '').replace('\n', ''))
        if corridor_light != corridor_light_last:        
            now = datetime.datetime.now()
            requests.post(
                'http://ilnurgi1.ru/arduino/', 
                data={
                    'light': data,
                    'date': now.strftime('%Y.%m.%d %H:%m:%S')
                })
            print 'post',
            corridor_light_last = corridor_light
