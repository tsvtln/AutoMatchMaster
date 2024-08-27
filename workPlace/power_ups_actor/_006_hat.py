"""
- No user interaction after activating.

When activating Booster, the Hat will Appear and spawns 3
Random Special Pieces. When your turn Ends, The Special pieces will be Removed.
It will be Good with Detonator Perk and with the Blow em' Up mode,
so it can Explode the Special Pieces to make sure that They will not Disappear.
"""
import time
import pyautogui


class HatPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        time.sleep(5)
