from time import sleep

def setTimer(hours, mins, secs):
	hours = hours/60
	timerTime = hours/60 + mins/60 + secs
	sleep(timerTime)

if __name__ == "__main__":
	print("Testing")
	print("Please set timer(hours).")
	hours = input()
	print("Please set timer(minutes).")
	mins = input()
	print("Please set timer(seconds).")
	secs = input()
	hours = hours/60
	timerTime = hours/60 + mins/60 + secs
	sleep(timerTime)
	while True:
		print("ctrl c to stop")
		print("Ring ring ring ring ring ring ring")
		print("alarm is going off")
		print("im done sleeping")
