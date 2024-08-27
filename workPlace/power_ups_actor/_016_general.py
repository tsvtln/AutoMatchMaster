"""
- Only activate. ~10sec cd
"""
import time
import pyautogui


class GeneralPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        time.sleep(10)
