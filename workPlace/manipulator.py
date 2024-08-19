import pyautogui
import time

# from workPlace.helper import HelperFunctions, TkinterWorker, TakeScreenshot
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
        # print(type_mode, game_mode_name)
        # print(self.power_up)








