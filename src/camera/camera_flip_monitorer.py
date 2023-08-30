"""
Die Kamera dreht sich um 180°, wenn sie einen  bestimmten tilt-Wert überschreitet. Es wurde festgestellt, dass nach einer Drehung der Kamera
die y-Komponente des continous-move-Geschwindikeitsvektors einen inversen Effekt hat. Dies führt dazu, dass nach einer Kameradrehung die Kamera in die
genau entgegengesetzte y-Richtung steuert als man beabsichtigt. Weiterhin wurde festgestellt, dass die Inversion automatisch wieder aufgehoben wird, wenn
die Kamera stillsteht.

Um ein korrektes Tracking zu gewährleisten, muss das Vorliegen des Kameraflips erkannt werden und dann durch ein kurzzeitiges Stillstehen behandelt werden.
CameraFlipMonitorer erkennt den Flip der Kamera.
"""


class CameraFlipMonitorer():

    def __init__(self,pan) -> None:
        self.camera_is_flipped = False
        self.pan = pan
     

    def check_camera_flipped(self, current_pan):

        if(abs(self.pan-current_pan)>170):
            self.camera_is_flipped = not self.camera_is_flipped
        self.pan = current_pan

