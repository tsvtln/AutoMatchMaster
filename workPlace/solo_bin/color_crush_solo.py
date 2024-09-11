import os

from workPlace.base_vars import Locations
from workPlace.m3x_walker import MatrixWalker
from workPlace.decide_and_act import DecideAndAct
from workPlace.power_ups_actor.power_up_actorator import PowerUpActorator as PUA

import numpy as np
from PIL import Image
from typing import Any, Union, Dict, List, Optional

from workPlace.helper import HelperFunctions as WH

from skimage.metrics import structural_similarity as ssim


class ColorCrushSolo(Locations):
    def __init__(self, power_up: str):
        super().__init__()
        self.power_up = power_up
        self._power_up_charge: Optional[int] = 0
        self.power_collected: int = 0
        self.turns_left: int = 6
        # self.screenshooter = WH.take_screenshot()
        self.state_image: Image.Image = Image.open(self.screenshot_state_path)
        self.board_matrix: List[List[str]] = []
        self.tiles: Dict[str, Any] = {}
        self.m3x_walker: MatrixWalker = MatrixWalker
        self.worker()

    @property
    def power_up_charge(self):
        return self._power_up_charge

    @power_up_charge.setter
    def power_up_charge(self, value):
        if self.power_up in ['Rocket', 'Duck', 'Broom']:
            self._power_up_charge = 6
        else:
            self._power_up_charge = 7
        print(f"Power-up charge set to {self._power_up_charge}")

    def tile_scanner(self):
        WH.tile_scanner(self.state_image, self.tiles_state_path)

    def tile_analyzer(self) -> None:
        self.tiles = WH.tile_analyzer(self.tiles_state_path, self.comp_tiles_path, self.tiles)

    def matrix_maker(self):
        if self.board_matrix:
            self.board_matrix.clear()
        if not self.board_matrix:
            self.board_matrix = [['' for _ in range(7)] for _ in range(7)]
        for k, v in self.tiles.items():
            _, row, col = k.split('_')
            row, col = int(row) - 1, int(col) - 1
            if v == 'blue':
                self.board_matrix[row][col] = 'B'
            elif v == 'green':
                self.board_matrix[row][col] = 'G'
            elif v == 'orange':
                self.board_matrix[row][col] = 'O'
            elif v == 'purple':
                self.board_matrix[row][col] = 'P'
            elif v == 'red':
                self.board_matrix[row][col] = 'R'
            elif v == 'yellow':
                self.board_matrix[row][col] = 'Y'
            else:
                print('M4TR1X 3RR0R')

    def worker(self):
        # WH.take_screenshot(self.screenshot_state_path)
        check_power_level = WH.power_checker(self.screenshot_state_path, self.power_state_dump)
        print(f'Value of CPL: {check_power_level}')
        if check_power_level:
            if self.power_up in ['Rocket', 'Duck', 'Broom']:
                self.power_collected = 6
            else:
                self.power_collected = 7
        if self.power_collected == self._power_up_charge:
            self.power_collected = 0
            print('POWER UP#######################')
            PUA(self.power_up)
            self.worker()
        self.tile_scanner()
        self.tile_analyzer()
        self.matrix_maker()
        self.m3x_walker = MatrixWalker(self.board_matrix)
        triple_coords, quad_coords, penta_coords, quad_bool, penta_bool = self.m3x_walker.get_result()
        DecideAndAct(triple_coords, quad_coords, penta_coords, quad_bool, penta_bool)
        self.turns_left -= 1
        if self.turns_left > 0:
            self.worker()
