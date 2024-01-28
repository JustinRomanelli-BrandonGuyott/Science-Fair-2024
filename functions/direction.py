import RPi.GPIO as GPIO            

def retract():
    GPIO.setwarnings(False)          # Disables "pin in use" warning
    GPIO.setmode(GPIO.BCM)          # BCM = Broadcom GPIO numbers; BOARD = Pin numbers
    GPIO.setup(23, GPIO.OUT)           
    GPIO.output(23, 0)          # Set power on Pin 23 to 0v

def extend():
    GPIO.setwarnings(False)          # Disables "pin in use" warning
    GPIO.setmode(GPIO.BCM)          # BCM = Broadcom GPIO numbers; BOARD = Pin numbers
    GPIO.setup(23, GPIO.OUT)           
    GPIO.output(23, 1)          # Engage 3.3v of power on Pin 23
