import pigpio
pi = pigpio.pi()

# Sets the correct speed level       
def set_speed(speed): 

    if (speed == 0):
        pi.hardware_PWM(18, 0, 0)
        print("Speed 0")

    elif (speed == 1):
        pi.hardware_PWM(18, 18000, 825000)
        print("Speed 1")
    
    elif (speed == 2):
        pi.hardware_PWM(18, 10000, 850000)
        print("Speed 2")
    
    elif (speed == 3):
        pi.hardware_PWM(18, 10000, 900000)
        print("Speed 3")
    
    elif (speed == 4):
        pi.hardware_PWM(18, 10, 1000000)
        print("Speed 4")

    else:
        print("Speed is not set to the correct values")
