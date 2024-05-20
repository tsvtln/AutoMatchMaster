import os
import sys


class Locations:
    def __init__(self):
        self.workdir = Locations.workdir()
        # current_state
        self.screenshot_state_path = os.path.join(self.workdir, 'collector', 'current_state.png')
        # tkinter power-ups vars:
        self.power_rocket_pic = os.path.join(self.workdir, 'etc', '001.jpg')
        self.power_duck_pic = os.path.join(self.workdir, 'etc', '002.jpg')
        self.power_paint_pic = os.path.join(self.workdir, 'etc', '003.jpg')
        self.power_jelly_pic = os.path.join(self.workdir, 'etc', '004.jpg')
        self.power_rocket2_pic = os.path.join(self.workdir, 'etc', '005.jpg')
        self.power_hat_pic = os.path.join(self.workdir, 'etc', '006.jpg')
        self.power_owl_pic = os.path.join(self.workdir, 'etc', '007.jpg')
        self.power_broom_pic = os.path.join(self.workdir, 'etc', '008.jpg')
        self.power_lazer_pic = os.path.join(self.workdir, 'etc', '009.jpg')
        self.power_wand_pic = os.path.join(self.workdir, 'etc', '010.jpg')
        self.power_dragon_pic = os.path.join(self.workdir, 'etc', '011.jpg')
        self.power_baloons_pic = os.path.join(self.workdir, 'etc', '012.jpg')
        self.power_lightning_pic = os.path.join(self.workdir, 'etc', '013.jpg')
        self.power_leprichaun_pic = os.path.join(self.workdir, 'etc', '014.jpg')
        self.power_bug_pic = os.path.join(self.workdir, 'etc', '015.jpg')
        self.power_general_pic = os.path.join(self.workdir, 'etc', '016.jpg')
        self.power_train_pic = os.path.join(self.workdir, 'etc', '017.jpg')
        self.power_spray_pic = os.path.join(self.workdir, 'etc', '018.jpg')
        self.power_robot_pic = os.path.join(self.workdir, 'etc', '019.jpg')
        self.power_ufo_pic = os.path.join(self.workdir, 'etc', '020.jpg')
        self.power_cobra_pic = os.path.join(self.workdir, 'etc', '021.jpg')

    @staticmethod
    def workdir():
        if getattr(sys, 'frozen', False):
            # Find if program is running as a standalone executable
            return os.path.abspath(os.path.join(os.path.dirname(sys.executable)))
        else:
            # Return this path if program is in dev mode or .py instance.
            return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
