import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servoPIN = 11
# GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(2.5)
try:
	while True:
		p.ChangeDutyCycle(5)
		time.sleep(0.5)
		# p.ChangeDutyCycle(7.5)
		# time.sleep(0.5)
		# p.ChangeDutyCycle(10)
		# time.sleep(0.5)
		# p.ChangeDutyCycle(12.5)
		# time.sleep(0.5)
		# p.ChangeDutyCycle(10)
		# time.sleep(0.5)
		# p.ChangeDutyCycle(7.5)
		# time.sleep(0.5)
		# p.ChangeDutyCycle(5)
		# time.sleep(0.5)
		# p.ChangeDutyCycle(2.5)
		# time.sleep(0.5)
except KeyboardInterrupt:
	p.stop()
finally:
	GPIO.cleanup()
