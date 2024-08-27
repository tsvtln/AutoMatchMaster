"""
- No user interaction after activating.
"""
import time
import pyautogui


class OwlPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        time.sleep(5)
