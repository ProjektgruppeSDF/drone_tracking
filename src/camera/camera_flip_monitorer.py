class CameraFlipMonitorer():

    camera_is_flipped = False

    previous_pan = None
    previous_tilt = None
    current_pan = None
    current_tilt = None

    def check_camera_flipped(self, current_pan, current_tilt):
        self.previous_pan = self.current_pan
        self.previous_tilt = self.current_tilt
        self.current_pan = current_pan
        self.current_tilt = current_tilt

        # Logik

