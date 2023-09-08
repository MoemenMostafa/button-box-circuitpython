import board
import digitalio
import rotaryio
import time
import usb_hid
import keypad
from hid_gamepad import Gamepad

# Set up the HID Gamepad
gp = Gamepad(usb_hid.devices)

# KeyMatrix setup
km = keypad.KeyMatrix(
    row_pins=(board.GP0, board.GP1),
    column_pins=(board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8),
)


# Encoders setup
encoder_pins = [(board.GP10, board.GP11), (board.GP13, board.GP14), (board.GP16, board.GP17), (board.GP19, board.GP20)]
encoders = [rotaryio.IncrementalEncoder(pinA, pinB) for pinB, pinA in encoder_pins]

encoder_buttons_pins = [board.GP12, board.GP15, board.GP18, board.GP21]
encoder_buttons = [digitalio.DigitalInOut(pin) for pin in encoder_buttons_pins]
for encoder_button in encoder_buttons:
    encoder_button.direction = digitalio.Direction.INPUT
    encoder_button.pull = digitalio.Pull.UP

# Define the keycodes for the buttons
button_keycodes = [
    1, 2, 3, 4, 5, 6, 7,
    8, 9, 10, 11, 12, 13, 14
]

# Define the keycodes for the encoders
encoder_keycodes = [
    [15, 16, 17],
    [18, 19, 20],
    [21, 22, 23],
    [24, 25, 26]
]

# Initialize encoder buttons state list with False value
encoder_button_state = [False for i in range(len(encoder_buttons))]

# Keypress and release
def keyPress(key):
    gp.press_buttons(key)

def keyRelease(key):
    gp.release_buttons(key)

# Main loop
while True:
    # KeyMatrix reading and handling
    event = km.events.get()
    if event:
        if event.pressed:
            print(event)
            keyPress(button_keycodes[event.key_number])
        if event.released:
            print(event)
            keyRelease(button_keycodes[event.key_number])



    # Encoders reading and handling
    for idx, encoder in enumerate(encoders):
        if encoder.position != 0:
            print("Encoder {}: Position = {}".format(idx, encoder.position))
            print("encoder_keycode = {}".format(encoder_keycodes[idx][encoder.position + 1]))
            keyPress(encoder_keycodes[idx][encoder.position + 1])
            keyRelease(encoder_keycodes[idx][encoder.position + 1])
            encoder.position = 0

    # Encoder Buttons reading and handling
    for idx, encoder_button in enumerate(encoder_buttons):
        if not encoder_button.value and not encoder_button_state[idx]:
            print("encoder_buttons {} Pressed".format(idx))
            keyPress(encoder_keycodes[idx][1])
            encoder_button_state[idx] = True
        if encoder_button.value and encoder_button_state[idx]:
            print("encoder_buttons {} Released".format(idx))
            keyRelease(encoder_keycodes[idx][1])
            encoder_button_state[idx] = False


    time.sleep(0.01)  # Add a small delay to avoid flooding the USB connection
