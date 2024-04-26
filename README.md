# Simple Python Keylogger

This Python script is a simple keylogger designed for educational purposes to demonstrate how keystroke logging can be implemented using Python. It captures keystrokes, logs them to a file, and helps understand the basics of handling keyboard events in Python.

## Disclaimer

This keylogger is intended for educational use only. Do not use it to capture keystrokes without the explicit permission of the keyboard owner. Unauthorized use of this script for capturing keystrokes on computers that do not belong to you is illegal and unethical.

## Features

- Logs all keystrokes including special keys like Shift, Caps Lock, Enter, and Space.
- Stores keystrokes in a log file in the current working directory.
- Converts keystrokes into readable sentences, taking into account the status of Caps Lock and Shift keys.

## Requirements

- Python 3.x
- pynput library

## Setup and Installation

1. Ensure Python 3.x is installed on your system.
2. Install the `pynput` library using pip:
```pip install pynput```
4. Clone this repository or download the script to your local machine.

## Usage

To run the keylogger, execute the script from the command line:
```python keylogger.py```


The script will start logging keystrokes to a file named `key_log.txt` in the same directory as the script. To stop the keylogger, press the `Esc` key.

## How it Works

The keylogger uses the `pynput.keyboard` module to listen to keyboard events. The script defines two functions: `on_press` and `on_release`:
- `on_press` handles key press events, logging alphanumeric characters directly and translating special characters based on whether Shift or Caps Lock is active.
- `on_release` detects when special keys (like Shift) are released and handles the exit condition when the Esc key is pressed.

The script also logs the final sentence constructed from the typed characters when the Esc key is pressed to demonstrate the practical use of capturing and processing keyboard input.

## Contributions

Contributions to this project are welcome, especially those that enhance functionality or improve the ethical safeguards of the script.





