from pynput import keyboard
import serial

arduino = serial.Serial('COM10', 9600, timeout=.1)
isDataPSent = False
isDataRSent = False
def on_press(key):
    global isDataPSent
    global isDataRSent
    if key == keyboard.Key.alt_l and not isDataPSent:
        isDataPSent = True
        isDataRSent = False
        arduino.write(bytes("1\n", 'utf-8'))


def on_release(key):
    global isDataPSent
    global isDataRSent
    if key == keyboard.Key.alt_l and not isDataRSent:
        isDataRSent = True
        isDataPSent = False
        arduino.write(bytes("0\n", 'utf-8'))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()