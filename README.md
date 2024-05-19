# Raspberry Pi Zero H Shifter (circuitpython)

A DIY H Shifter project using a Raspberry Pi Zero microcontroller. This project allows you to create a custom H shifter input device with support for 6-7 speeds and R.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project utilizes a Raspberry Pi Zero microcontroller and hall sensors to create the H shifter

## Features

- 6 to 7 gears and R
- Emulates a gamepad using the `adafruit_hid` library.

## Hardware Requirements

To build this project, you will need the following hardware components:

- Raspberry Pi Zero
- Hall sensors
- Multiplexer
- 3d printed parts
- Custom pcb
- 20cm aluminum pipe or metal tread with a diameter of 8mm (m8)
- USB cable for connecting to a computer

## Software Requirements

This project relies on the following software libraries:

- [CircuitPython](https://circuitpython.org/)
- [adafruit_hid Library](https://circuitpython.readthedocs.io/projects/hid/en/latest/)

Make sure you have CircuitPython installed on your Raspberry Pi Pico and the required libraries available.

## Setup

1. Install CircuitPython on your Raspberry Pi Zero if not already installed.

2. Install the required libraries (`adafruit_hid`) on your Raspberry Pi Pico lib folder.

3. Upload the provided Python script to your Raspberry Pi Pico root using your preferred method.

## Usage

Use the Raspberry Pi Zero H shifter to simulate custom input controls. The script handles button presses emulating a gamepad.

## Customization

Customize the button box behavior by modifying the provided Python script. You can change keycodes, button layouts, and encoder functions to suit your specific requirements.

## Contributing

If you'd like to contribute to this project, please open an issue or create a pull request on the GitHub repository. Your contributions and suggestions are welcome!

## License

This project is licensed under the [MIT License](LICENSE.md). See the [LICENSE](LICENSE.md) file for details.
