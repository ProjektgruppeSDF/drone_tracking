"""
Die Kamera dreht sich um 180°, wenn sie einen  bestimmten tilt-Wert überschreitet. Es wurde festgestellt, dass nach einer Drehung der Kamera
die y-Komponente des continous-move-Geschwindikeitsvektors einen inversen Effekt hat. Dies führt dazu, dass nach einer Kameradrehung die Kamera in die
genau entgegengesetzte y-Richtung steuert als man beabsichtigt. Um ein korrektes Tracking zu gewährleisten, muss das Vorliegen des Kameraflips erkannt werden
und dann anschließend durch Flippen der y-Komponente des continous-move-Geschwindikeitsvektors behandelt werden. CameraFlipMonitorer erkennt den Flip der Kamera.
"""


class CameraFlipMonitorer():

    def __init__(self,pan) -> None:
        self.camera_is_flipped = 1
        self.pan = pan
     

    def check_camera_flipped(self, current_pan):
        # erster Check: bei Kameradrehung ändert sich der pan von einem frame zum nächsten um 180°
        # zweiter Check: geht pan gerade von -180° zu 180° über? Falls ja, false alarm für Kameraflip
        if((abs(self.pan-current_pan)>170) & (abs(self.pan-current_pan)<190)):
            self.camera_is_flipped = self.camera_is_flipped * -1
        self.pan = current_pan
        return self.camera_is_flipped

