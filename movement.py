import RPi.GPIO as GPIO
import time

MOTION = 13 #pin 13 used for motion detector

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(MOTION, GPIO.IN)


var = 1

while var == 1:
	if GPIO.input(MOTION)==GPIO.HIGH:
		print "Movement detected!"

	else:
		print "No movement"

	time.sleep(5)
