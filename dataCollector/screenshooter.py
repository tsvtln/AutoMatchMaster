import os
import pyautogui

from workPlace.helper import Locations


class TakeScreenshot(Locations):
    def __init__(self):
        super().__init__()

    def take_screenshot(self):
        # Takes screenshot of the current state of the game.
        screenshot_dir = 'collector'
        screenshot_name = 'current_state.png'
        screenshot_path = os.path.join(self.workdir, screenshot_dir, screenshot_name)
        take_screenshot = pyautogui.screenshot()
        take_screenshot.save(screenshot_path)

