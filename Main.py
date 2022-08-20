import RPI.gpio as gpio
import time
from long-sleep import setTimer

def setup():	# Setup for the GPIO pins on the raspberry pi
	#	set the pin names to the digital names, rather than mechanical
	gpio.setmode(gpio.bcm)
	#	set the four pins that will be used for controlling leds
	gpio.setup(5, gpio.OUT)
	gpio.setup(6, gpio.OUT)
	gpio.setup(13, gpio.OUT)
	gpio.setup(19, gpio.OUT)
	#	set the red led pin
	gpio.setup(24, gpio.OUT)
	#	setup the pins for reading buttons
	gpio.setup(20, gpio.IN)
	gpio.setup(21, gpio.IN)

def alarmSet():	# A function for setting the alarm
	

def alarm():	# The code for the alarm going off
	

def preAlarm():	# The code for preparing for the alarm to go off
	

def snooze():	# The function for snoozing the alarm
	

def postAlarm():	# The code for when you don't snoooze/stop the alarm
	

def wait(): # The code to wait for the alarm time
	

def destroy():	# What happens when you kill the program via ctrl c
  gpio.cleanup()

if __name__ == '__main__':
	setup():
		try:
			alarmSet()
			wait()
			alarm()
		except KeyboardInterrupt: # KeyboardInterrupt = ctrl c
			destroy()
