import numpy as np
from datetime import datetime
from datetime import timedelta

# TODO: Zeitstempel Variable
class TargetLossMonitorer():

    target_lost_threshold_sec = 5

    def __init__(self) -> None:
        self.time_since_last_detection = np.inf
        self.time_last_detection = datetime.now()
        self.is_target_lost = True

    def target_detection(self, dt):
        self.time_last_detection = dt
        self.is_target_lost = False

    def no_target_detection(self, dt):
        timedelta_last_detection = dt- self.time_last_detection
        timedelta_inS= timedelta_last_detection/timedelta(seconds=1)
        if (timedelta_inS >= self.target_lost_threshold_sec):
            self.is_target_lost = True
        pass