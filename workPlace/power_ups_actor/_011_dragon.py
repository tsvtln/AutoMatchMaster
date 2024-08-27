"""
When Activating, The Dragon will Appear. Choose a Move that you want to Burn, And the Dragon will Burn 3 Columns
"""
import time
import pyautogui


class DragonPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        time.sleep(1)
