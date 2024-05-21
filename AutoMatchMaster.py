# # runner
# from dataCollector.screenshooter import TakeScreenshot
#
# runner = TakeScreenshot()
#
# runner.take_screenshot()
# #
from workPlace.helper import TkinterWorker

from workPlace.manipulator import Manipulator

try:
    auto_match = TkinterWorker()
except Exception as e:
    if isinstance(e, IndexError):
        print('You need to select a checkbox!')
    else:
        print(f"An error occurred: {e}")
        input('Press Enter button to continue...')
