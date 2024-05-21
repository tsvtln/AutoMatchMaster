import pyautogui
import time

from workPlace.helper import HelperFunctions
from workPlace.base_vars import Locations


class Manipulator(Locations):
    def __init__(self, power_up, game_mode, debug=False):
        super().__init__()
        self.power_up = power_up
        self.game_mode = game_mode
        self.debug = debug







