from workPlace.power_ups_actor._001_rocket import RocketPWUP
from workPlace.power_ups_actor._002_duck import DuckPWUP
from workPlace.power_ups_actor._003_paint import PaintPWUP
from workPlace.power_ups_actor._004_jelly import JellyPWUP
from workPlace.power_ups_actor._005_rocket2 import Rocket2PWUP
from workPlace.power_ups_actor._006_hat import HatPWUP
from workPlace.power_ups_actor._007_owl import OwlPWUP
from workPlace.power_ups_actor._008_broom import BroomPWUP
from workPlace.power_ups_actor._009_lazer import LazerPWUP
from workPlace.power_ups_actor._010_wand import WandPWUP
from workPlace.power_ups_actor._011_dragon import DragonPWUP
from workPlace.power_ups_actor._012_baloons import BaloonsPWUP
from workPlace.power_ups_actor._013_lightning import LightningPWUP
from workPlace.power_ups_actor._014_leprichaun import LeprichaunPWUP
from workPlace.power_ups_actor._015_bug import BugPWUP
from workPlace.power_ups_actor._016_general import GeneralPWUP
from workPlace.power_ups_actor._017_train import TrainPWUP
from workPlace.power_ups_actor._018_spray import SprayPWUP
from workPlace.power_ups_actor._019_robot import RobotPWUP
from workPlace.power_ups_actor._020_ufo import UFOPWUP
from workPlace.power_ups_actor._021_cobra import CobraPWUP


class PowerUpActivator:
    def __init__(self, pwup):
        self.power_up = pwup
        self.activate()

    def activate(self):
        # c_name = f'{self.power_up}PWUP'
        # c_ref = globals()[c_name]
        # c_inst = c_ref()
        # c_inst.runner()
        globals()[f'{self.power_up}PWUP']().runner()

