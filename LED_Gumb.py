import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.IN)
GPIO.setup(3, GPIO.OUT)
gumb_pritisnjen = False
led_prizgana = False
while True:
	gumb_pritisnjen = GPIO.input(24)
	if gumb_pritisnjen:
		led_prizgana = not led_prizgana
        GPIO.output(3, led_prizgana)
        time.sleep(0.5)
		
