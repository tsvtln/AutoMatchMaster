"""
- Single click a peace (no further action needed after that)
    • When Activating, you need to Select a Color on the Board. While Picking a color, it will remove All pieces from
     the chosen color kind. You can only Pick one color when using it.
    • Use the wand on the Red Circles, so the opponent could not use their Booster.
    • When you are in Gem Grab Studio, use the wand on the Purple color, so you can earn more Points.
    • When you are in Multipier Mushrooms Studio, use the wand on the Color that has Mushrooms,
     so you can earn more Points, and Increase your Multipier.
    • When you are in Dustville Duel Studio, use the wand on the Orange Color, so you can remove the Outlaws from
     the board, and Earn More Points.
    • If there is a Special Piece on the Board, choose the color that the Special Pieces is painted on,
     and then it will blow up.
"""
import time
import pyautogui

class WandPWUP:
    def __init__(self):
        self.runner()

    def runner(self):
        pcx, pcy = (751, 312)
        pyautogui.leftClick(pcx, pcy)
        pix, piy = (947, 693)
        pyautogui.leftClick(pix, piy)
        time.sleep(8)
