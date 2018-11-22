import RPi.GPIO as GPIO
import time
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
PIN_DATA=8

GPIO.setup(PIN_DATA,GPIO.IN)
try:
	print GPIO.input(PIN_DATA)
	time.sleep(1)
except:
	print "ERROR"
finally:
	GPIO.cleanup()