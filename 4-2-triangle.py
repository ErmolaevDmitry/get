import RPi.GPIO as GPIO
import time

def decimal2binary(number):
        return [int(i) for i in bin(number)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()
GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

T = 5
i = 0

try:
	T = int(input())
	while True:
		time.sleep(T / 256)
		GPIO.output(dac, decimal2binary(i % 256))
		i += 1
finally:
	GPIO.output(dac, [0]*8)
	GPIO.cleanup()
