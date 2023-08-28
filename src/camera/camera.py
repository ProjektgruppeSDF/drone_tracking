from .camera_specs import *
from .camera_url_queries import query_videostream_flipped_, query_get_orientation, get_query_continous_move

import requests
import cv2
from datetime import datetime


class Camera():

    def __init__(self) -> None:
        self.video = cv2.VideoCapture(query_videostream_flipped_)

    def capture_image(self):
        dt = datetime.now()
        ret,image = self.video.read()
        return image,dt
    
    def get_camera_ptz_orientation(self):
        response = requests.get(query_get_orientation)

        response_text = response.text

        ptz = {}
        lines = response_text.split('\n')
        for line in lines:
            if '=' in line:
                key , value = line.split('=')
                if(key == "pan" or key == "tilt" or key == "zoom"):
                    ptz[key] = float(value.strip())
        return ptz

# TODO: der Faktor 1/25 sollte zoomabhängig gewählt sein
    def move_camera(self, tracking_result,zoom):
        try:
            #Auflösung ist 800x450 und 400,225 ist der Mittelpunkt des Bildes
            abweichungX = 400 - int(tracking_result[0]) 
            abweichungy = 225 - int(tracking_result[1])
            print(abweichungX)
            print(abweichungy)
            
            #Kamerabewegung durch Richtung/Geschwindigkeit
            #Kamerabewgung abhängig von Abstand zum Mittelpunkt des Bildes sowie des Zooms
            vx = -(int(abweichungX) / 25)
            vy = (int(abweichungy) / 25 )
            url = get_query_continous_move(vx, vy)
            requests.get(url)
 
        except:
            print("keine bounding box")
        
