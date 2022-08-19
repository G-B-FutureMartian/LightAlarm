import RPI.gpio as gpio
import time

def setup():	# Setup for the GPIO pins on the raspberry pi
	

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
