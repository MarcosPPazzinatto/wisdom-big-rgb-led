# Project Overview

This project aims to control the RGB LED on the RoboCore BlackBoard Wisdom using Python.  
The RGB LED is capable of displaying red, green, and blue colors, and reacts to button presses on the board.

## Objective

To explore the behavior of the onboard RGB LED through direct GPIO programming in Python, allowing interactive color changes via the built-in button.

## Main Files

### 1. `main.py`

This file is used for **autoboot** on the board.  
When the board starts, it automatically executes this script.  
It is typically used to initialize or route execution logic (e.g., call the `button_rgb_led` logic).

### 2. `button_rgb_led.py`

This script contains the **core logic** for controlling the RGB LED.  
It listens for button presses and cycles through LED colors (Red → Green → Blue → Off) with each press.

The file includes:
- GPIO pin definitions for the RGB LED
- Button input configuration
- A color cycling algorithm based on a counter

## Execution Flow

When the board powers on:
1. `main.py` is executed automatically.
2. `main.py` may directly call or import logic from `button_rgb_led.py`.
3. The RGB LED starts responding to button interactions.

## Future Improvements

- Add fade transitions between colors
- Include debounce logic for button press
- Expand to include multi-button control or external triggers

