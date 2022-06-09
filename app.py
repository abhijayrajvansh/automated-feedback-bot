#/
#    author:   abhijayrajvansh
#    created:  09.06.2022 16:36:38
#/
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

def fill_feedback():
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.1)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.1)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.1)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.1)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
print("Get ready, and point your cursor at the right position...")
time.sleep(3)

while(True):
    fill_feedback()