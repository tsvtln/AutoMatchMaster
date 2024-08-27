"""
- Only activate. ~8sec cd.

When Activating the Booster, Roxy will Appear and Starts Spraying Pieces in Random Color.
There's a 90% Chance it will make a Special Piece.

Roxy is Amazing at Blow em' Up, because she Doesn't need to Blow up any Piece!
It automatically Blows up Every Special Piece in the Board.
"""
import time
import pyautogui

class SprayPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        time.sleep(8)
