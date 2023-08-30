from enum import Enum

class Modes(Enum):
    SCAN_MODE = 0
    TRACK_MODE = 1

class ProgramMode():

    def __init__(self, mode) -> None:
        self.mode = mode

    def enter_scan_mode(self):
        self.mode = Modes.SCAN_MODE
        #Camera.enter_scan_mode
        pass

    def enter_track_mode(self):
        self.mode = Modes.TRACK_MODE
        #tracker.reinitialize_kalman()
        pass

