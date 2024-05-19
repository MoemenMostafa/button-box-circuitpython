import board
import analogio
import time
import digitalio
import usb_hid
from hid_shifter import Gamepad


# Set up the Multiplixer
hallsens1 = digitalio.DigitalInOut(board.GP8)
hallsens1.direction = digitalio.Direction.INPUT

analog = analogio.AnalogIn(board.GP26)

digital1 = digitalio.DigitalInOut(board.GP0)
digital1.direction = digitalio.Direction.OUTPUT

digital2 = digitalio.DigitalInOut(board.GP1)
digital2.direction = digitalio.Direction.OUTPUT

digital3 = digitalio.DigitalInOut(board.GP2)
digital3.direction = digitalio.Direction.OUTPUT

# End of multiplixer setup

# Set up Variables
hall1 = 0
hall2 = 0
hall3 = 0
hall4 = 0
hall5 = 0
hall6 = 0
hall7 = 0
hall8 = 0
gear = 0
prevGear = 0

# Set up the HID Shifter
shifter = Gamepad(usb_hid.devices)

# Keypress and release
def shiftIn(gear):
    shifter.press_buttons(gear)
    print(gear)

def shiftOut():
    shifter.release_all_buttons()

while True:
    sleepTime = 0.00125
    time.sleep(sleepTime)
    digital1.value = False
    digital2.value = False
    digital3.value = False
    hall1 = analog.value

    time.sleep(sleepTime)
    digital1.value = True
    digital2.value = False
    digital3.value = False
    hall2 = analog.value

    time.sleep(sleepTime)
    digital1.value = False
    digital2.value = True
    digital3.value = False
    hall3 = analog.value

    time.sleep(sleepTime)
    digital1.value = True
    digital2.value = True
    digital3.value = False
    hall4 = analog.value

    time.sleep(sleepTime)
    digital1.value = False
    digital2.value = False
    digital3.value = True
    hall5 = analog.value

    time.sleep(sleepTime)
    digital1.value = True
    digital2.value = False
    digital3.value = True
    hall6 = analog.value

    time.sleep(sleepTime)
    digital1.value = False
    digital2.value = True
    digital3.value = True
    hall7 = analog.value

    time.sleep(sleepTime)
    digital1.value = True
    digital2.value = True
    digital3.value = True
    hall8 = analog.value

#     print(hall1, hall2, hall3, hall4, hall5, hall6, hall7, hall8)

    threshold = 27000

    if hall8 < threshold + 2000:
        gear = 8
    elif hall7 < threshold:
        gear = 1
    elif hall3 < threshold:
        gear = 2
    elif hall5 < threshold:
        gear = 5
    elif hall6 < threshold:
        gear = 3
    elif hall1 < threshold:
        gear = 6
    elif hall2 < threshold:
        gear = 4
    else:
        gear = 0


    if gear != prevGear:
        shiftOut()
        if gear > 0:
            shiftIn(gear)

    prevGear = gear
#     print((0, gear, 8))
