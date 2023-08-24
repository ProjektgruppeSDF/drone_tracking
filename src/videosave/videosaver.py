import cv2

class Videosaver:

    def __init__(self) -> None:
        self.video = cv2.VideoWriter('Versuch1.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, (800,450))
        
    def write(self, image):
        self.video.write(image) 