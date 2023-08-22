

import requests
import cv2
import numpy as np
import os 


class Camera():

    def __init__(self) -> None:
        self.video = requests.get('http://192.168.11.103/axis-cgi/mjpg/video.cgi', stream=True)
        if not self.video.status_code == 200:
            print(self.video.status_code)
            raise Exception("Kamera nicht erreichbar.")
        self.bytes_ = bytes()


    def capture_image(self):   
        for chunk in self.video.iter_content(chunk_size=1024):
            self.bytes_ += chunk
            a = self.bytes_.find(b'\xff\xd8')
            b = self.bytes_.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = self.bytes_[a:b+2]
                self.bytes_ = self.bytes_[b+2:]
                image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                return image

    def move_camera(self, tracking_result):
        pass