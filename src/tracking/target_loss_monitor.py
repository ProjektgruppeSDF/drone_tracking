import numpy as np

# TODO: Zeitstempel Variable
class TargetLossMonitorer():

    target_lost_threshold_sec = 3

    def __init__(self) -> None:
        self.time_since_last_detection = np.inf
        self.is_target_lost = True

    def target_detection(self, dt):
        self.time_since_last_detection = 0
        self.is_target_lost = False

    def no_target_detection(self, dt):
        # self.time_since_last_detection += dt
        # if (self.time_since_last_detection >= self.target_lost_threshold_sec):
        #     self.is_target_lost = True
        pass