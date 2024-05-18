import os
import sys


class HelperFunctions:
    @staticmethod
    def workdir():
        if getattr(sys, 'frozen', False):
            # Find if program is running as a standalone executable
            return os.path.abspath(os.path.join(os.path.dirname(sys.executable)))
        else:
            # Return this path if program is in dev mode or .py instance.
            return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class Locations:
    def __init__(self):
        self.workdir = HelperFunctions.workdir()
