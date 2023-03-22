import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 10000)
pwm.start(0)

try:
	while True:
		i = int(input())
		if i > 100:
			print("value must be less than 100")
			continue
		pwm.ChangeDutyCycle(i)
		print(i / 100 * 3.3)
finally:
	pwm.stop()
	GPIO.output(18, 0)
	GPIO.cleanup()

