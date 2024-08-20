import time

start_time = time.time()

# # runner
# from workPlace.helper import TakeScreenshot
# runner = TakeScreenshot()
#
# runner.take_screenshot()
# # #
#
# from workPlace.solo_bin.color_crush_solo import ColorCrushSolo

# Initialize ColorCrushSolo instance
# tileScan = ColorCrushSolo('powerUp')

# Perform tile scanning and analysis
# tileScan.tile_scanner()
# tileScan.tile_analyzer()
#
# # Generate the board matrix
# tileScan.matrix_maker()


########################
########################
from workPlace.helper import TkinterWorker

# from workPlace.manipulator import Manipulator

try:
    auto_match = TkinterWorker()
except Exception as e:
    if isinstance(e, IndexError):
        print('You need to select a checkbox!')
    else:
        print(f"An error occurred: {e}")
        input('Press Enter button to continue...')


end_time = time.time()
execution_time = end_time - start_time
print(round(execution_time, 2))
