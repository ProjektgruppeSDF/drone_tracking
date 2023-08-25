import cv2

class Videosaver:

    def __init__(self) -> None:
        self.video = cv2.VideoWriter('Versuch1.avi', 
                         cv2.VideoWriter_fourcc('I','4','2','0'),
                         15, (1920,1080))
        
    def write(self, image):
        self.video.write(image) 