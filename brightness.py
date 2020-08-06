#!/usr/bin/env python3

import RPi.GPIO as GPIO
import ADC0832
import os
import datetime
import time
import smbus
import ds18b20
import i2c_lcd1602

screen = i2c_lcd1602.Screen(bus=1, addr=0x27, cols=16, rows=2)

line = "Personal Project"
screen.enable_backlight()
screen.clear()


ADC0832.setup()
#path_w = 'brightness.txt'


#for i in range(10):
# 72 で 1 時間、72x6 時間で 432 288 4 時間、864 で 12 時間

def sensor(line):
#    screen.cursorTo(0, 0)
#    screen.println(line)

# 温度検知
    t = ds18b20.dsb20Read()
    t = round(t, 1)
    m = '%f' %t
    m = m[:5]

# 輝度検知
    res = ADC0832.getResult()

    dt_now = datetime.datetime.now()
    l = dt_now.strftime('%Y/%m/%d,%H:%M') + ',' + str(res) + ',' + str(m)
    screen.cursorTo(0, 0)
    screen.println('photoregist: ' + str(res))
    screen.cursorTo(1, 0)
    screen.println(' Temp: ' + str(m) + ' C  ')
    screen.clear()
    return l

#        if not os.path.isfile(path_w):
#            with open(path_w, mode='w') as f:
#                f.writelines(l)
#        else:
#            with open(path_w, mode='a') as f:
#                f.writelines(l)
#
#        time.sleep(3)
#
#else:
#
#    ADC0832.destroy()
#    GPIO.cleanup()
#    print ('Cleanup ADC!')

def loop():
    while True:
        for i in range(10):
            sensor()
            time.sleep(3)
        input("input CR")

def subloop():
        while True:
                screen = i2c_lcd1602.Screen(bus=1, addr=0x27, cols=16, rows=2)
                line = "Personal Project"
                screen.enable_backlight()
                screen.clear()
                ADC0832.setup()
                line = sensor(line)
                return line

# Main starts here
#if __name__ == '__main__':
#    try:
#        loop()
#    except KeyboardInterrupt:
#            ADC0832.destroy()
#            GPIO.cleanup()
#            print ('Cleanup ADC!')

