import os

from workPlace.base_vars import Locations
from workPlace.m3x_walker import MatrixWalker
from workPlace.decide_and_act import DecideAndAct

import numpy as np
from PIL import Image

from workPlace.helper import TakeScreenshot
from skimage.metrics import structural_similarity as ssim


class ColorCrushSolo(Locations):
    def __init__(self, power_up):
        super().__init__()
        self.power_up = power_up
        self._power_up_charge = None
        self.turns_left = 6
        self.screenshooter = TakeScreenshot()
        self.state_image = Image.open(self.screenshot_state_path)
        self.board_matrix = []
        self.tiles = {}
        self.worker()
        self.m3x_walker = MatrixWalker

    @property
    def powerUpChargeSetter(self):
        return self._power_up_charge

    @powerUpChargeSetter.setter
    def powerUpChargeSetter(self, value):
        if self.power_up == 'Jelly':
            value = 7
        self._power_up_charge = value

    def tile_scanner(self):
        # Regions of boxes with tiles
        # line - row x 7
        tile_regions = [
            # line 1
            (671, 430, 743, 502),  # 1 1
            (750, 430, 822, 502),  # 1 2
            (829, 430, 901, 502),  # 1 3
            (907, 430, 979, 502),  # 1 4
            (986, 430, 1058, 502),  # 1 5
            (1064, 430, 1136, 502),  # 1 6
            (1143, 430, 1215, 502),  # 1 7
            # line 2
            (671, 509, 743, 581),  # 2 1
            (750, 509, 822, 581),  # 2 2
            (829, 509, 901, 581),  # 2 3
            (907, 509, 979, 581),  # 2 4
            (986, 509, 1058, 581),  # 2 5
            (1064, 509, 1136, 581),  # 2 6
            (1143, 509, 1215, 581),  # 2 7
            # line 3
            (671, 588, 743, 660),  # 3 1
            (750, 588, 822, 660),  # 3 2
            (829, 588, 901, 660),  # 3 3
            (907, 588, 979, 660),  # 3 4
            (986, 588, 1058, 660),  # 3 5
            (1064, 588, 1136, 660),  # 3 6
            (1143, 588, 1215, 660),  # 3 7
            # line 4
            (671, 666, 743, 738),  # 4 1
            (750, 666, 822, 738),  # 4 2
            (829, 666, 901, 738),  # 4 3
            (907, 666, 979, 738),  # 4 4
            (986, 666, 1058, 738),  # 4 5
            (1064, 666, 1136, 738),  # 4 6
            (1143, 666, 1215, 738),  # 4 7
            # line 5
            (671, 745, 743, 817),  # 5 1
            (750, 745, 822, 817),  # 5 2
            (829, 745, 901, 817),  # 5 3
            (907, 745, 979, 817),  # 5 4
            (986, 745, 1058, 817),  # 5 5
            (1064, 745, 1136, 817),  # 5 6
            (1143, 745, 1215, 817),  # 5 7
            # line 6
            (671, 823, 743, 895),  # 6 1
            (750, 823, 822, 895),  # 6 2
            (829, 823, 901, 895),  # 6 3
            (907, 823, 979, 895),  # 6 4
            (986, 823, 1058, 895),  # 6 5
            (1064, 823, 1136, 895),  # 6 6
            (1143, 823, 1215, 895),  # 6 7
            # line 7
            (671, 902, 743, 974),  # 7 1
            (750, 902, 822, 974),  # 7 2
            (829, 902, 901, 974),  # 7 3
            (907, 902, 979, 974),  # 7 4
            (986, 902, 1058, 974),  # 7 5
            (1064, 902, 1136, 974),  # 7 6
            (1143, 902, 1215, 974)  # 7 7
        ]

        # extract tiles
        for i, region in enumerate(tile_regions):
            tile_region_crop = self.state_image.crop(region)
            tile_save_path = os.path.join(self.tiles_state_path, f'tile_{i + 1}.png')
            tile_region_crop.save(tile_save_path)

    def tile_analyzer(self):
        if not self.tiles:
            self.tiles = {f'tile_{r}_{c}': '' for r in range(1, 8) for c in range(1, 8)}
        else:
            self.tiles.clear()
            self.tiles = {f'tile_{r}_{c}': '' for r in range(1, 8) for c in range(1, 8)}
        for tile_num in range(1, 50):
            tile_state_image = Image.open(os.path.join(self.tiles_state_path, f'tile_{tile_num}.png'))
            tile_state_image_np = np.array(tile_state_image)

            # find tile color
            for filename in os.listdir(self.comp_tiles_path):
                comp_image = Image.open(os.path.join(self.comp_tiles_path, filename))
                comp_image_np = np.array(comp_image)

                # calculate SSI
                smaller_side = min(tile_state_image_np.shape[0], tile_state_image_np.shape[1],
                                   comp_image_np.shape[0], comp_image_np.shape[1])
                win_size = min(smaller_side, 3)
                similarity_index, _ = ssim(tile_state_image_np, comp_image_np, win_size=win_size, full=True)
                similarity_index = float(f"{similarity_index:.2f}")

                if similarity_index > 0.8:
                    filename = filename[:-6]
                    r = (tile_num - 1) // 7 + 1
                    c = (tile_num - 1) % 7 + 1
                    self.tiles[f'tile_{r}_{c}'] = filename
                    break
        # for k, v in self.tiles.items():
        #     print(f'Key: {k}\nValue: {v}\n\n')

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
        # for line in self.board_matrix:
        #     print(line)

    def worker(self):
        # self.screenshooter.take_screenshot()
        self.tile_scanner()
        self.tile_analyzer()
        self.matrix_maker()
        self.m3x_walker = MatrixWalker(self.board_matrix)
        triple_coords, quad_coords, penta_coords, quad_bool, penta_bool = self.m3x_walker
        DecideAndAct(triple_coords, quad_coords, penta_coords, quad_bool, penta_bool)
