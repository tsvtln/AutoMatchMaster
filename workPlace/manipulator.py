import pyautogui
import time

# from workPlace.helper import HelperFunctions, TkinterWorker, TakeScreenshot
from workPlace.solo_bin.color_crush_solo import ColorCrushSolo
from workPlace.base_vars import Locations


class Manipulator(Locations):
    def __init__(self, power_up, game_mode, debug=False):
        super().__init__()
        self.power_up = power_up
        self.game_mode = game_mode
        self.debug = debug
        self.game_mode_hopper()

    def game_mode_hopper(self):
        type_mode, game_mode_name = self.game_mode[0].split('_')

        if game_mode_name == 'ColorCrush' and type_mode == 'SOLO':
            ColorCrushSolo(self.power_up)
            
        # print(type_mode, game_mode_name)
        # print(self.power_up)








