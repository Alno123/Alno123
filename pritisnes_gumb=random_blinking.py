import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

while True:
    if (GPIO.input(24)):
	    for i in range(0, 20) :
		    GPIO.output(random.sample([3, 10, 15, 16, 12, 5], 3), True)
		    time.sleep(0.1)
		    GPIO.output(random.sample([3, 10, 15, 16, 12, 5], 3), False)
		    time.sleep(0.1)
		    GPIO.output(3, False)
		    GPIO.output(10, False)
		    GPIO.output(15, False)
		    GPIO.output(16, False)
		    GPIO.output(12, False)
		    GPIO.output(5, False)

			

