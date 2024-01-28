# Functions to set the speed of the system (including turning off).
import pigpio

pi = pigpio.pi()

# Turn power off
def power_off():
    pi = pigpio.pi()
    pi.hardware_PWM(18, 0, 0)

# Set the speed to 1, slowest
def set_speed_1():
    pi = pigpio.pi()
    pi.hardware_PWM(18, 18000, 825000)

# Set the speed to 2, slower
def set_speed_2():
    pi = pigpio.pi()
    pi.hardware_PWM(18, 10000, 750000)

# Set the speed to 3, faster
def set_speed_3():
    pi = pigpio.pi()
    pi.hardware_PWM(18, 5000, 750000)

# Set the speed to 4, fastest
def set_speed_4():
    pi = pigpio.pi()
    pi.hardware_PWM(18, 10, 1000000)
