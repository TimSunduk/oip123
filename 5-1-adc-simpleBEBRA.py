import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
troyka = 17
comp = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(decimal):
    return [int(elem) for elem in bin(decimal)[2:].zfill(8)]

def num2dac(value):
    b = decimal2binary(value)
    GPIO.output(dac,b)
    return b    

def adc():
    num = 0
    while (num != 256):
        num2dac(num)
        time.sleep(1)
        comparatorValue = GPIO.input(comp)
        
        if comparatorValue == 0:
            return num
        num += 1
    return 256

try:
    while (True):
        decimal = adc()
        voltage = 3.3 * decimal /256
        print("ADC value = {:^3}, input voltage = {:.2f}".format(decimal, voltage))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
