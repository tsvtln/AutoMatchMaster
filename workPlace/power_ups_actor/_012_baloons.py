"""
- Only activate
"""
import time
import pyautogui

class BaloonsPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        time.sleep(5)