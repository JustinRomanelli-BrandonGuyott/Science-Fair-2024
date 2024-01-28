import RPi.GPIO as GPIO
from functions.pwm import set_speed

# red led is GPIO 27, green is GPIO 22
def emergency_stop(should_stop = False):
   
    if (should_stop):
        # GREEN LED OFF; RED LED ON
        print("Emergency Stop")
        set_speed(0)
  
    else:
        # GREEN LED ON; RED LED OFF
        print("Safe to operate")

def warning_light(activated = False):
    green_led = 22
    red_led = 27
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(green_led, GPIO.OUT)
    GPIO.setup(red_led, GPIO.OUT)
    
    if (activated):
        GPIO.output(green_led, 0)
        GPIO.output(red_led, 1)
    else:
        GPIO.output(green_led, 1)
        GPIO.output(red_led, 0)