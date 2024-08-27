"""
- Only activate. ~8sec cd
"""
import time
import pyautogui


class TrainPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        time.sleep(8)
