"""
- Pick a peace (single click) and afterward no user interaction is needed.
"""

import time
import pyautogui


class JellyPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        pix, piy = (947, 693)
        pyautogui.leftClick(pix, piy)
        time.sleep(8)
