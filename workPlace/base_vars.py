import os
import sys


class Locations:
    def __init__(self):
        self.workdir = Locations.workdir()
        # paths
        self.screenshot_state_path = os.path.join(self.workdir, 'collector', 'current_state.png')  # current state
        self.tiles_state_path = os.path.join(self.workdir, 'collector', 'tiles')  # extracted tiles
        self.comp_tiles_path = os.path.join(self.workdir, 'etc', 'comp', 'comp_tiles')  # tiles to compare to
        self.state_dump_dir = os.path.join(self.workdir, 'etc', 'state_dumps')  # state dump dir
        self.power_comp_path = os.path.join(self.workdir, 'etc', 'comp', 'comp_power.png')

        # tkinter power-ups vars:
        self.power_rocket_pic = os.path.join(self.workdir, 'etc', '001.png')
        self.power_duck_pic = os.path.join(self.workdir, 'etc', '002.png')
        self.power_paint_pic = os.path.join(self.workdir, 'etc', '003.png')
        self.power_jelly_pic = os.path.join(self.workdir, 'etc', '004.png')
        self.power_rocket2_pic = os.path.join(self.workdir, 'etc', '005.png')
        self.power_hat_pic = os.path.join(self.workdir, 'etc', '006.png')
        self.power_owl_pic = os.path.join(self.workdir, 'etc', '007.png')
        self.power_broom_pic = os.path.join(self.workdir, 'etc', '008.png')
        self.power_lazer_pic = os.path.join(self.workdir, 'etc', '009.png')
        self.power_wand_pic = os.path.join(self.workdir, 'etc', '010.png')
        self.power_dragon_pic = os.path.join(self.workdir, 'etc', '011.png')
        self.power_baloons_pic = os.path.join(self.workdir, 'etc', '012.png')
        self.power_lightning_pic = os.path.join(self.workdir, 'etc', '013.png')
        self.power_leprichaun_pic = os.path.join(self.workdir, 'etc', '014.png')
        self.power_bug_pic = os.path.join(self.workdir, 'etc', '015.png')
        self.power_general_pic = os.path.join(self.workdir, 'etc', '016.png')
        self.power_train_pic = os.path.join(self.workdir, 'etc', '017.png')
        self.power_spray_pic = os.path.join(self.workdir, 'etc', '018.png')
        self.power_robot_pic = os.path.join(self.workdir, 'etc', '019.png')
        self.power_ufo_pic = os.path.join(self.workdir, 'etc', '020.png')
        self.power_cobra_pic = os.path.join(self.workdir, 'etc', '021.png')

        # power state dump
        self.power_state_dump = os.path.join(self.workdir, 'etc', 'power_state.png')

        # comp dir
        self.compare_dir = os.path.join(self.workdir, 'etc', 'comp')

    @staticmethod
    def workdir():
        if getattr(sys, 'frozen', False):
            # Find if program is running as a standalone executable
            return os.path.abspath(os.path.join(os.path.dirname(sys.executable)))
        else:
            # Return this path if program is in dev mode or .py instance.
            return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
