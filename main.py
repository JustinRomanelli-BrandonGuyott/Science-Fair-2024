from multiprocessing import Process
from functions.direction import extend, retract
from functions.ir_receiver import find_ir_receiver
from functions.pwm import set_speed
from functions.commands import convert_commands
from functions.distance_sensor import distance_watchdog, safe_to_close, initialize_distance
from functions.safety_system import emergency_stop
from functions.weight_sensor import weight_watchdog

# **** FUNCTIONS ****

# Waits until a command is received, then returns it.
def receive_command():
    # Get the remote
    ir_receiver = find_ir_receiver()

    # Read a value from the remote and run the respective code repeatedly.
    while True:

        event = ir_receiver.read_one()
        while not(event) or not(event.value):
            event = ir_receiver.read_one()

        # Convert value --> plaintext --> interpret action to be done
        interpret_commands(convert_commands(event.value))

# Interpret the commands to do action
def interpret_commands(command):
    global power_on
    global speed
    
    # If the user presses the Speed (Volume) Up button, raise the speed by 1 if it is not already at the maximum
    if command == "Volume Up" and speed < 4 and power_on:
        speed += 1
        set_speed(speed)
    
    # If the user presses the Speed (Volume) Down button, lower the speed by 1 if it is not already at the minimum
    elif command == "Volume Down" and speed > 1 and power_on:
        speed -= 1
        set_speed(speed)

    # Closing the window (will not work if system is turned off or emergency_stop(True) is triggered (see functions.safety_system.py))
    elif command == "Channel Down":
        trigpin = 16
        echopin = 12
        window_length = 69
        
        initialize_distance(trigpin, echopin)
        if safe_to_close(trigpin, echopin, window_length):   # 9(trigpin, echopin, window_length)
            extend()
    
    # Opening the window (will not work if system is turned off or emergency_stop(True) is triggered (see functions.safety_system.py))
    elif command == "Channel Up":
        retract()

    # Turn on the power
    elif command == "Power Button":
        power_on = True
        set_speed(speed)
        emergency_stop(False)

    # Turn off the power
    elif command == "F Button":
        power_on = False
        set_speed(0)
    
    
    elif command == "Mute" and power_on: # Set to the lowest speed
        speed = 1
        set_speed(speed)
    

# Main function, get the rpi and wait for commands to be sent on repeat.
def main():
    global power_on
    global speed

    # Intialize variables
    power_on = False
    speed = 4

    emergency_stop(False)

    # Create the processes (multiprocessing) to run the code in tandem
    p1 = Process(target=receive_command)
    p2 = Process(target=distance_watchdog)
    p3 = Process(target=weight_watchdog)

    # Start the processes.
    p1.start()
    p2.start()
    p3.start()

# Run the main function.
if (__name__ == "__main__"):
    main()
