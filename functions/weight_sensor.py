from functions.safety_system import emergency_stop, warning_light
from functions.distance_sensor import safe_to_close, initialize_distance
from time import sleep
from dependencies.hx711 import HX711
import RPi.GPIO as GPIO

# Arbitrarily set based on experimentation values
referenceUnit = 1000

global hx
global weight_list
hx = HX711(5, 6)
weight_list = []

def measure_weight():
    # Get the value of the weight sensor
    val = abs(int(hx.get_weight()))
    return val


# RECODE THIS FUNCTION IF TIME
def check_weight():
    variant = 10
    max_weight = 50


    weight = measure_weight()
    #print(weight)
    weight_list.append(weight)
    weight_difference = weight_list[-1] - weight_list[-2]
    
    if weight_difference >= variant or weight > max_weight: # IMPORTANT: Keep the or
    
        warning_light(True)
    
        while not(weight_difference <= -variant) and weight >= max_weight:  # IMPORTANT: Keep the and
            print("In The Loop")
            if (GPIO.input(23) == 1): # Necessary adjustment since window nags wood on open
                emergency_stop(True)
            
            weight = measure_weight()
            print(weight)
            weight_list.append(weight)
            weight_difference = weight_list[-1] - weight_list[-2]
            sleep(0.1)
            
            if len(weight_list) >= 3:
                weight_list.pop(0)

        emergency_stop(False)
    
    if not(safe_to_close(16, 12, 72)):
        warning_light(True)
    else:
        warning_light(False)

    if len(weight_list) >= 3:
        weight_list.pop(0)
    
    sleep(0.1)


def weight_watchdog():
    hx.set_reading_format("MSB", "MSB")

    hx.set_reference_unit(referenceUnit)

    hx.reset()

    hx.tare()

    # This gets the first weight value to start
    weight_list.append(measure_weight())
    
    initialize_distance(16, 12)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)

    while True:
        check_weight()
