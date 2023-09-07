# Raspberry Pi Pico Button Box (circuitpython)

A DIY button box project using a Raspberry Pi Pico microcontroller. This project allows you to create a custom button input device with support for buttons, encoders, and encoder buttons.

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

This project utilizes a Raspberry Pi Pico microcontroller to create a button box capable of simulating a gamepad or other input devices. It can be used for gaming, simulation, or any application requiring custom input controls.

## Features

- Button support with customizable keycodes.
- Encoder support with customizable keycodes.
- Encoder button support with customizable keycodes.
- Emulates a gamepad using the `adafruit_hid` library.

## Hardware Requirements

To build this project, you will need the following hardware components:

- [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/)
- Buttons (e.g., momentary push buttons)
- Encoders (with encoder buttons, if desired)
- Wiring and soldering tools
- Project enclosure or box
- USB cable for connecting to a computer

## Software Requirements

This project relies on the following software libraries:

- [CircuitPython](https://circuitpython.org/)
- [adafruit_hid Library](https://circuitpython.readthedocs.io/projects/hid/en/latest/)
- [Keypad Library](https://circuitpython.readthedocs.io/projects/keypad/en/latest/)

Make sure you have CircuitPython installed on your Raspberry Pi Pico and the required libraries available.

## Setup

1. Connect the buttons and encoders to the Raspberry Pi Pico's GPIO pins. Refer to your wiring diagram for button and encoder pin connections.

2. Install CircuitPython on your Raspberry Pi Pico if not already installed.

3. Install the required libraries (`adafruit_hid`) on your Raspberry Pi Pico lib folder.

4. Upload the provided Python script to your Raspberry Pi Pico root using your preferred method.

## Usage

Use the Raspberry Pi Pico button box to simulate custom input controls. The script handles button presses, encoder movements, and encoder button presses, emulating a gamepad.

## Customization

Customize the button box behavior by modifying the provided Python script. You can change keycodes, button layouts, and encoder functions to suit your specific requirements.

## Contributing

If you'd like to contribute to this project, please open an issue or create a pull request on the GitHub repository. Your contributions and suggestions are welcome!

## License

This project is licensed under the [MIT License](LICENSE.md). See the [LICENSE](LICENSE.md) file for details.
