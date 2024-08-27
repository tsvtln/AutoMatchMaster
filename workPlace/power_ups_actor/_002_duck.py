"""
When Activating, the Duck will Spawn and will remove the Middle Row. In The Past, it removed the Bottom Row.
- No user interaction after activating.
"""
import time
import pyautogui


class DuckPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        time.sleep(5)
