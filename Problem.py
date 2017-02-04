import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

CODE - {'A' :'.-'}
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    CODE - {'A' :'.-'}
NameError: name 'CODE' is not defined


def dot():
    GPIO.output(3, True)
    time.sleep(0.25)
    GPIO.outptut(3, False)
    time.sleep(0.25)

	
def dash():
    GPIO.output(3, True)
    time.sleep(0.5)
    GPIO.outptu(3, False)
    time.sleep(0.25)

	

code - {"A" :".-"}
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    code - {"A" :".-"}
NameError: name 'code' is not defined

CODE-{'A' :'.-'}
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    CODE-{'A' :'.-'}
NameError: name 'CODE' is not defined

