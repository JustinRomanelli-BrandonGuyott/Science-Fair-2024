import RPi.GPIO as GPIO
from time import sleep, time
from functions.safety_system import warning_light

# *** FUNCTIONS ***
def initialize_distance(trigpin, echopin):

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(trigpin, GPIO.OUT)
    GPIO.setup(echopin, GPIO.IN)

def get_distance(trigpin, echopin):
    GPIO.output(trigpin, True)
    sleep(0.5)
    GPIO.output(trigpin, False)
    while GPIO.input(echopin) == 0:
        pass

    echoStartTime = time()
    while GPIO.input(echopin) == 1:
        pass
    echoEndTime = time()

    echoTime = echoEndTime - echoStartTime
    calculated_distance = round(echoTime * 17150, 2)

    return calculated_distance

def safe_to_close(trigpin, echopin, window_length):

    distance = round(get_distance(trigpin, echopin), 2)
    #print(distance) # TESTING CODE

    if distance < (window_length - 5) or distance > (window_length + 5): return False
    return True

def distance_watchdog():
    trigpin = 16
    echopin = 12
    window_length = 69

    initialize_distance(trigpin, echopin)

    while True:
        distance = round(get_distance(trigpin, echopin), 2)
        while distance < (window_length - 5) or distance > (window_length + 5):
            warning_light(True)
            distance = round(get_distance(trigpin, echopin), 2)
            sleep(0.1)
            
        warning_light(False)

        sleep(0.1)
