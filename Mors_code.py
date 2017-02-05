import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

CODE = {"A" :".-",
    "B" :"-...",
    "C" :"-.-.",
    "D" :"-..",
    "E" :".",
    "F" :"..-.",
    "G" :"--.",
    "H" :"....",
    "I" :"..",
    "J" :".---",
    "K" :"-.-",
    "L" :".-..",
    "M" :"--",
    "N" :"-.",
    "O" :"---",
    "P" :".--.",
    "Q" :"--.-",
    "R" :".-.",
    "S" :"...",
    "T" :"-",
    "U" :"..-",
    "V" :"...-",
    "W" :".---",
    "X" :"-..-",
    "Y" :"-.--",
    "Z" :"--..",
    "1" :".----",
    "2" :"..---",
    "3" :"...--",
    "4" :"....--",
    "5" :".....",
    "6" :"-....",
    "7" :"--...",
    "8" :"---..",
    "9" :"----.",}
list1 = 3, 5, 10, 12, 15, 16
RANDOM = random.sample([list1], 1)

def dot():
    GPIO.output(list1, True)
    time.sleep(0.25)
    GPIO.output(list1, False)
    time.sleep(0.25)
  
def slash():
    GPIO.output(list1, True)
    time.sleep(0.75)
    GPIO.output(list1, False)
    time.sleep(0.25)

try:
    while True:
        input = raw_input("Kaj bi zeleli poslati?")
        for letter in input:
            for symbol in CODE[letter.upper()]:
                if symbol == "-":
                    slash()
                elif symbol == ".":
                    dot()
                else:
                    time.sleep(0.5)
                time.sleep(0.5)
except: KeyboardInterrupt

