

import requests
import cv2
import numpy as np
import os 
from datetime import datetime


class Camera():

    def __init__(self) -> None:
        self.video = requests.get('http://192.168.11.103/axis-cgi/mjpg/video.cgi', stream=True)
        if not self.video.status_code == 200:
            print(self.video.status_code)
            raise Exception("Kamera nicht erreichbar.")
        self.bytes_ = bytes()


    def capture_image(self):  
        dt = datetime.now() 
        for chunk in self.video.iter_content(chunk_size=1024):
            self.bytes_ += chunk
            a = self.bytes_.find(b'\xff\xd8')
            b = self.bytes_.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = self.bytes_[a:b+2]
                self.bytes_ = self.bytes_[b+2:]
                image = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                return cv2.flip(image, 0),dt

    def move_camera(self, tracking_result):
        try:
            abweichungX = 400 - tracking_result[0] #Auflösung ist 800x450 und 400,225 ist der Mittelpunkt des Bildes
            abweichungy = 225 - tracking_result[1]
            #bewegungX = -(abweichungX / 60)
            #bewegungY = -(abweichungy /60)
            #url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?rpan='+str(bewegungX)
            #response = requests.get(url)
            #url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?rtilt='+str(bewegungY)
            #response = requests.get(url)
            bewegungX = -(abweichungX / 8)
            bewegungY = -(abweichungy /8)
            url = 'http://192.168.11.103/axis-cgi/com/ptz.cgi?continuouspantiltmove='+str(int(bewegungX))+','+str(int(bewegungY))
            response = requests.get(url)
 
        except:
            print("keine bounding box")
        pass