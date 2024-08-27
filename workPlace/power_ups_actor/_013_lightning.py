"""
When you Activate the Booster, You have to Pick a Color to Remove from the Board. When choosing a Color,
There will Be an Electric Chain that will Remove the Chosen Color, and the Nearby Pieces.
"""
import time
import pyautogui


class LightningPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        pix, piy = (947, 693)
        pyautogui.leftClick(pix, piy)
        time.sleep(8)
