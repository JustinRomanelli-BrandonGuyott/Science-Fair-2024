import evdev

# Get all of the devices, if the rpi is found, then return that.
def find_ir_receiver():
        devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
        for device in devices:
                if (device.name == "gpio_ir_recv"):
                        print("Located GPIO IR Receiver at", device.path, "\n")
                        return device
        print("No device found.")
