#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import requests
import datetime as d
from threading import Thread

GPIO.setmode(GPIO.BOARD)

pin_to_circuit = 8
servoPIN = 11
GPIO.setup(servoPIN, GPIO.OUT)
motor_state=False

url='https://api.thingspeak.com/update'
key='WQM4PC5U0A40Q6RT'

def rc_time(pin_to_circuit):
	count = 0
	GPIO.setup(pin_to_circuit, GPIO.OUT)
	GPIO.output(pin_to_circuit, GPIO.LOW)
	time.sleep(0.1)
	GPIO.setup(pin_to_circuit, GPIO.IN)
	while(GPIO.input(pin_to_circuit) == GPIO.LOW):
		count += 1
	return count

try:
	p = GPIO.PWM(servoPIN, 50)

	while True:
		moisture=rc_time(pin_to_circuit)
		print(moisture)
		if moisture>100:
			data={'api_key':key,'field1':moisture}
			try:
			    requests.post(url,data)
			except:
				print("Post error")
			p.start(2.5)
			while True:
				moisture1=rc_time(pin_to_circuit)
				print(moisture1)
				if moisture1<100:
					p.stop()
					break
except:
	print "except"
finally:
	GPIO.cleanup()