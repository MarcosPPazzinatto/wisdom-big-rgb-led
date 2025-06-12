# Wisdom RGB LED - Button Control

This project controls the RGB LED on the RoboCore BlackBoard Wisdom using Python.  
The LED can shine in red, green, or blue, and its color changes every time the onboard button is pressed.

## Board

- **Model:** RoboCore BlackBoard Wisdom
- **Component:** Main onboard RGB LED (Red, Green, Blue)
- **Interaction:** Button GPIO (Pin 27)

## Language

- **Python (MicroPython or CircuitPython)**
- Script: `button_rgb_led.py`

## Project Behavior

- The RGB LED starts off
- Each button press switches the LED to a different color in the following order:
  1. Red
  2. Green
  3. Blue
  4. Off
- The cycle repeats

## File

- Main.py - Main file
- button_rgb_led.py - File core

## How to Run

1. Flash your board with MicroPython or CircuitPython
2. Upload `button_rgb_led.py` or `main.py` to the board
3. Press the onboard button and observe the LED color change

## Notes

This project is part of a larger exploration of the RoboCore Wisdom board using Python instead of visual blocks.

## License

Free to use for educational and personal projects. Contributions are welcome.  
