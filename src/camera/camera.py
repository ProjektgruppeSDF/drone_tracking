import cv2

class Camera():

    def __init__(self) -> None:
        self.video = cv2.VideoCapture("resources/BeispielVideoWebcam.mp4")

    def capture_image(self):
        # TODO: non success Fall behandeln
        success, img = self.video.read()
        return img

    def move_camera(self, tracking_result):
        pass