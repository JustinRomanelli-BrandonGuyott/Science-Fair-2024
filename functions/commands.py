# Convert the numerical values into (human-readable) command strings.
def convert_commands(event_value):
    commands = {
        0: "No Button Pressed",
        1: None,
        2: "Channel Up",
        3: "Channel Down",
        4: "Volume Down",
        5: "Volume Up",
        6: "Mute",
        7: "F Button",
        460557: "Power Button"

    }

    command = commands.get(event_value, None)

    return command
