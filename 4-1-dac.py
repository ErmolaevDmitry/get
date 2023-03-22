import RPi.GPIO as GPIO

def decimal2binary(number):
	return [int(i) for i in bin(number)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 13, 19, 26]
dac.reverse()
GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

try:
	while True:
		b = input()
		if b == 'q':
			break
		try:
			i = int(b)
		except ValueError:
			print("value must be integer")
			continue
		if i > 255:
			print("value must be less than 255")
			continue
		if i < 0:
			print("value must be more positive")
			continue
		print(i / 255 * 3.3)
		GPIO.output(dac, decimal2binary(i))
finally:
	GPIO.output(dac, [0 for i in dac])
	GPIO.cleanup()

