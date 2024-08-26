import os

from workPlace.base_vars import Locations
from workPlace.m3x_walker import MatrixWalker
from workPlace.decide_and_act import DecideAndAct
from workPlace.power_ups_actor.power_up_actorator import PowerUpActorator as PUA

import numpy as np
from PIL import Image

import workPlace.helper as WH
from skimage.metrics import structural_similarity as ssim


class ColorCrushSolo(Locations):
    def __init__(self, power_up):
        super().__init__()
        self.power_up = power_up
        self._power_up_charge = None
        self.power_collected = 0
        self.turns_left = 6
        self.screenshooter = WH.TakeScreenshot()
        self.state_image = Image.open(self.screenshot_state_path)
        self.board_matrix = []
        self.tiles = {}
        self.m3x_walker = MatrixWalker
        self.worker()

    @property
    def powerUpChargeSetter(self):
        return self._power_up_charge

    @powerUpChargeSetter.setter
    def powerUpChargeSetter(self, value):
        if self.power_up in ['Rocket', 'Duck', 'Broom']:
            value = 6
        else:
            value = 7
        self._power_up_charge = value

    def tile_scanner(self):
        WH.HelperFunctions.tile_scanner(self.state_image, self.tiles_state_path)

    def tile_analyzer(self):
        self.tiles = WH.HelperFunctions.tile_analyzer(self.tiles_state_path, self.comp_tiles_path, self.tiles)


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
        if self.power_collected == self._power_up_charge:
            PUA(self.power_up)
        # self.screenshooter.take_screenshot()
        self.tile_scanner()
        self.tile_analyzer()
        self.matrix_maker()
        self.m3x_walker = MatrixWalker(self.board_matrix)
        triple_coords, quad_coords, penta_coords, quad_bool, penta_bool = self.m3x_walker
        DecideAndAct(triple_coords, quad_coords, penta_coords, quad_bool, penta_bool)
