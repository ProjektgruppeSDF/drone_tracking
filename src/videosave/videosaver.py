import cv2
from config.global_config import camera_resolution, camera_fps

class Videosaver:

    def __init__(self) -> None:
        self.video = cv2.VideoWriter('Versuch1.avi', 
                         cv2.VideoWriter_fourcc('I','4','2','0'),
                         camera_fps, camera_resolution)
        
    def write(self, image):
        self.video.write(image) 